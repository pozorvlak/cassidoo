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
    b = recent[0]
    new_available = available | {b} if b is not None else available
    for a in available:
        new_recent = recent[1:] + [a]
        for tail in go(new_available - {a}, l - 1, new_recent, unused - {a}):
            yield [a] + tail


def playlists(n, l, k):
    return list(go(set(range(n)), l, [None] * k, set(range(n))))


def num_playlists(n, l, k):
    return len(playlists(n, l, k))


def test_example():
    assert num_playlists(3, 3, 1) == 6


@given(st.integers(1, 5), st.integers(1, 5))
def test_n_equals_l(n, k):
    assert num_playlists(n, n, k) == math.factorial(n)


@given(st.integers(1, 5), st.integers(1, 5), st.integers(1, 5))
def test_constraints_hold(n, l, k):
    for playlist in playlists(n, l, k):
        assert set(playlist) == set(range(n))
        for i, p in enumerate(playlist[:k]):
            assert p not in playlist[i + 1: i + k]
