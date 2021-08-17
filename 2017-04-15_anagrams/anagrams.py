"""
Write a function that takes in two strings and returns true if they are
anagrams.
"""

from collections import Counter

def anagrams(s, t):
    return Counter(s) == Counter(t)


def test_true():
    assert anagrams("foo", "oof")


def test_differing_counts():
    assert not anagrams("fooooo", "of")


def test_false():
    assert not anagrams("wilma", "fred")
