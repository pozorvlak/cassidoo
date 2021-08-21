#!/usr/bin/env python

"""
Given a rowIndex, return an array of the values in that row of Pascal’s Triangle.

Example:

$ pascals(0)
$ [1]
$ pascals(3)
$ [1,3,3,1]
"""

from math import factorial

import pytest

def pascals(rowIndex):
    x = 1
    p = rowIndex
    q = 1
    row = [1]
    while p > 0:
        x = (x * p) // q
        p -= 1
        q += 1
        row.append(x)
    return row


def test_example1():
    assert pascals(0) == [1]


def test_example2():
    assert pascals(3) == [1, 3, 3, 1]


def comb(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


@pytest.mark.parametrize("n", range(20))
def test_oracle(n):
    expected = [comb(n, k) for k in range(n + 1)]
    assert pascals(n) == expected


@pytest.mark.parametrize("n", range(20))
def test_oracle2(n):
    expected = [1]
    for i in range(n):
        expected = [1] + [expected[i] + expected[i + 1] for i in range(len(expected) - 1)] + [1]
    assert pascals(n) == expected
