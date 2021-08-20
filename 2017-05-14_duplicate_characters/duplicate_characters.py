"""
Write a function that takes in a string and returns the first duplicate character it finds.

Bonus points: write another function that takes in a string and removes all the duplicate characters.
"""

from collections import Counter

import pytest
from hypothesis import given, strategies as st


def first_dupe(s):
    seen = set()
    for c in s:
        if c in seen:
            return c
        seen.add(c)


def remove_dupes(s):
    seen = set()
    retval = ""
    for c in s:
        if c not in seen:
            retval += c
            seen.add(c)
    return retval


@pytest.mark.parametrize("s,expected", [
    ("aabb", "a"),
    ("abcdabz", "a"),
    ("abbb", "b"),
    ("abcde", None)
])
def test_first_dupe(s, expected):
    assert first_dupe(s) == expected


@given(st.text(min_size=1))
def test_remove_dupes(s):
    chars = set(s)
    deduped = remove_dupes(s)
    assert set(deduped) == chars
    assert set(Counter(deduped).values()) == {1}
