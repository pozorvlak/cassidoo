#!/usr/bin/env python

"""
Your music library contains N songs and your friend wants to listen to L
songs during your road trip (repeats are allowed). Make a playlist so that
every song is played at least once, and a song can only be played again only
if K other songs have been played. Return the number of possible playlists.
"""

import itertools
import math

from hypothesis import given
import hypothesis.strategies as st
from minizinc import Instance, Model, Solver

#====================================================================
# Solution 1: recursively calculate the actual playlists
#====================================================================
def go(available, l, recent, unused):
    if l < 1:
        yield []
        return
    if l < len(unused):
        return
    if l == len(unused):
        for perm in itertools.permutations(unused):
            yield list(perm)
        return
    for a in available:
        # Update the queue inside the loop, to handle the case k = 0
        new_recent = [a] + recent
        b = new_recent.pop()
        new_available = available - {a}
        if b is not None:
            new_available = new_available | {b}
        for tail in go(new_available, l - 1, new_recent, unused - {a}):
            yield [a] + tail


def playlists(n, l, k):
    return list(go(set(range(n)), l, [None] * k, set(range(n))))


def num_playlists(n, l, k):
    return len(playlists(n, l, k))


#====================================================================
# Solution 2: recursively calculate the number of playlists
#
# This is about twice as fast as explicitly calculating the playlists
#====================================================================
def go2(available, l, recent, unused):
    if l < 1:
        return 1
    if l < len(unused):
        return 0
    if l == len(unused):
        return math.factorial(len(unused))
    count = 0
    for a in available:
        # Update the queue inside the loop, to handle the case k = 0
        new_recent = [a] + recent
        b = new_recent.pop()
        new_available = available - {a}
        if b is not None:
            new_available = new_available | {b}
        count += go2(new_available, l - 1, new_recent, unused - {a})
    return count


def num_playlists2(n, l, k):
    return go2(set(range(n)), l, [None] * k, set(range(n)))


#====================================================================
# Solution 3: call a constraint-propagation solver with MiniZinc
#
# This is over 50x slower than solution 2 :-(
#====================================================================
def go3(n, l, k):
    # The supplied MIP solver doesn't support the "all_solutions"
    # flag, so we must use a CP solver. It's still about 2x faster
    # to use a MIP-style model, though.
    solver = Solver.lookup("chuffed")
    model = Model("./num_playlists.mzn")
    instance = Instance(solver, model)
    instance["N"] = n
    instance["L"] = l
    instance["K"] = k
    return instance.solve(all_solutions=True)


def playlists3(n, l, k):
    result = go3(n, l, k)
    one_indexed_playlists = [result[i, "playlist"] for i in range(len(result))]
    return [[i - 1 for i in playlist] for playlist in one_indexed_playlists]


def num_playlists3(n, l, k):
    return len(playlists3(n, l, k))


#====================================================================
# Tests
#====================================================================
def test_example():
    assert num_playlists(3, 3, 1) == 6


@given(st.integers(1, 5), st.integers(0, 5))
def test_n_equals_l(n, k):
    assert num_playlists(n, n, k) == math.factorial(n)


@given(st.integers(1, 5), st.integers(1, 5), st.integers(0, 5))
def test_constraints_hold(n, l, k):
    for playlist in playlists(n, l, k):
        assert set(playlist) == set(range(n))
        for i, p in enumerate(playlist[:k]):
            assert p not in playlist[i + 1: i + k]


@given(st.integers(1, 5), st.integers(1, 5), st.integers(0, 5))
def test_list_too_short(diff, l, k):
    assert num_playlists(l + diff, l, k) == 0


def test_example2():
    assert num_playlists2(3, 3, 1) == 6


@given(st.integers(1, 5), st.integers(0, 5))
def test_n_equals_l(n, k):
    assert num_playlists2(n, n, k) == math.factorial(n)


@given(st.integers(1, 5), st.integers(1, 5), st.integers(0, 5))
def test_list_too_short(diff, l, k):
    assert num_playlists2(l + diff, l, k) == 0


@given(st.integers(1, 5), st.integers(1, 5), st.integers(0, 5))
def test_solutions_agree(n, l, k):
    n1 = num_playlists(n, l, k)
    n2 = num_playlists2(n, l, k)
    n3 = num_playlists3(n, l, k)
    assert n1 == n2
    assert n3 == n2


@given(st.integers(1, 3), st.integers(1, 5), st.integers(0, 5))
def test_explicit_solutions_agree(n, l, k):
    assert sorted(playlists(n, l, k)) == sorted(playlists3(n, l, k))
