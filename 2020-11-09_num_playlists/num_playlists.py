#!/usr/bin/env python

"""
Your music library contains N songs and your friend wants to listen to L
songs during your road trip (repeats are allowed). Make a playlist so that
every song is played at least once, and a song can only be played again only
if K other songs have been played. Return the number of possible playlists.
"""

import itertools
from functools import reduce, lru_cache
from operator import mul
import math
import sys

from hypothesis import given
import hypothesis.strategies as st
from minizinc import Instance, Model, Solver
import pytest

#====================================================================
# Solution 1: recursively calculate the actual playlists
#====================================================================
def go(available, l, recent, unused):
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
def call_minizinc(model_file, n, l, k):
    # The supplied MIP solver doesn't support the "all_solutions"
    # flag, so we must use a CP solver. It's still about 2x faster
    # to use a MIP-style model, though.
    solver = Solver.lookup("chuffed")
    model = Model(model_file)
    instance = Instance(solver, model)
    instance["N"] = n
    instance["L"] = l
    instance["K"] = k
    return instance.solve(all_solutions=True)


def playlists3(n, l, k):
    result = call_minizinc("./num_playlists_mip.mzn", n, l, k)
    one_indexed_playlists = [result[i, "playlist"] for i in range(len(result))]
    return [[i - 1 for i in playlist] for playlist in one_indexed_playlists]


def num_playlists3(n, l, k):
    return math.factorial(n) * len(call_minizinc("./num_playlists_mip.mzn", n, l, k))


#====================================================================
# Solution 4: dynamic programming
#
# Translated from Ten Zhi-Yang (@tzyinc)'s JavaScript solution:
# https://codepen.io/Tzyinc/pen/VwjgLrW?editors=0011
#====================================================================
def num_playlists_dp(n, l, k):
    # playlists[i][j] will contain the number of length-i playlists 
    # which uses j songs out of our n-song library
    playlists = [[0] * (n + 1) for i in range(l + 1)]
    playlists[0][0] = 1 # the empty playlist contains no songs
    for i in range(1, l + 1):
        for j in range(1, n + 1):
            # Add an unused song to make a longer playlist with one more song
            playlists[i][j] += playlists[i - 1][j - 1] * (n - j + 1)
            # Add a previously-used song to make a longer playlist
            # with the same number of songs
            playlists[i][j] += playlists[i - 1][j] * max(j - k, 0)
    # Return the number of playlists that are long enough and use all the songs
    return playlists[l][n]


#====================================================================
# Solution 5: fold over a list
#
# Translated from Sameer Kolhar (@kolharsam)'s Haskell solution:
# https://repl.it/@SameerKolhar/Cassidys-Interview-Question-November-9#main.hs
#
# This calculates a different function, but is included for completeness.
#====================================================================
def product(xs):
    return reduce(mul, xs)


def num_playlists_fold(n, l, k):
    if n > l:
        return product(range(n - l + 1, n + 1))
    if n == l:
        return math.factorial(n)
    return product(
            reduce(
                lambda acc, x: [n] + acc if x % k == 0 else [acc[0] - 1] + acc,
                range(l, 0, -1),
                [n]
            )
        )


#====================================================================
# Solution 5: Stirling numbers
#
# Translated from Roman Gusev (@9z3)'s JavaScript solution:
# https://gist.github.com/102/4e52d86a0e93dbb20568974e588acab1#file-index-js
#====================================================================
@lru_cache(maxsize=None)
def stirling2(n, k):
    if n == k:
        return 1
    if n == 0 or k == 0:
        return 0
    if k > n:
        return 0
    return k * stirling2(n - 1, k) + stirling2(n - 1, k - 1)


def num_playlists_stirling(n, l, k):
    if n == l:
        return math.factorial(n)
    if n > l or (k > n and n < l) or n == 0 or l == 0:
        return 0
    return math.factorial(n) * stirling2(l - k, n - k)


#====================================================================
# Solution 6: Constraint-propagation with global constraint
#====================================================================
def num_playlists_cp(n, l, k):
    return len(call_minizinc("./num_playlists_cp.mzn", n, l, k)) * math.factorial(n)


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


@pytest.mark.skip('Broken by the symmetry-breaking constraint in the MiniZinc model')
@given(st.integers(1, 3), st.integers(1, 5), st.integers(0, 5))
def test_explicit_solutions_agree(n, l, k):
    assert sorted(playlists(n, l, k)) == sorted(playlists3(n, l, k))


@given(st.integers(1, 5), st.integers(1, 5), st.integers(0, 5))
def test_dp_solution_agrees(n, l, k):
    n2 = num_playlists2(n, l, k)
    n4 = num_playlists_dp(n, l, k)
    assert n4 == n2


@pytest.mark.skip('The fold-based solution calculates a different function')
@given(st.integers(1, 5), st.integers(1, 5), st.integers(0, 5))
def test_fold_solution_agrees(n, l, k):
    n2 = num_playlists2(n, l, k)
    n5 = num_playlists_fold(n, l, k)
    assert n5 == n2


@given(st.integers(1, 5), st.integers(1, 5), st.integers(0, 5))
def test_stirling_solution_agrees(n, l, k):
    n2 = num_playlists2(n, l, k)
    n6 = num_playlists_stirling(n, l, k)
    assert n6 == n2


def main(other_index):
    other_funcs = [
            num_playlists,
            num_playlists2,
            num_playlists3,
            num_playlists_dp,
            num_playlists_fold,
            num_playlists_stirling,
            num_playlists_cp
        ]
    other_func = other_funcs[other_index - 1]
    for n in range(0, 15):
        for l in range(0, 15):
            for k in range(0, 15):
                mine = num_playlists2(n, l, k)
                other = other_func(n, l, k)
                if mine != other:
                    print(f"n={n}, l={l}, k={k}, mine={mine}, other={other}")


if __name__ == '__main__':
    main(int(sys.argv[1]))
