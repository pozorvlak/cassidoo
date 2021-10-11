"""
An “odious number” is a non-negative number that has an odd number of 1s in its binary expansion. Write a function that returns true if a given number is odious.

Example:

$ isOdious(14)
$ true

$ isOdious(5)
$ false
"""

from collections import Counter


def is_odious(n):
    counts = Counter(bin(n))
    return counts['1'] % 2


def test_example1():
    assert is_odious(14)


def test_example2():
    assert not is_odious(5)
