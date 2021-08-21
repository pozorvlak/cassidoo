#!/usr/bin/env python

"""
Given an array of integers and a target value, return the number of pairs of array elements that have a difference equal to a target value.

Examples:

$ arrayDiff([1, 2, 3, 4], 1)
$ 3 // 2 - 1 = 1, 3 - 2 = 1, and 4 - 3 = 1
"""

from collections import Counter


def array_diff(xs, target):
    count = 0
    seen = Counter(xs)
    for x in xs:
        count += seen[x - target]
    return count


def test_example():
    assert array_diff([1, 2, 3, 4], 1) == 3


def test_repeat():
    assert array_diff([1, 1, 2], 1) == 2


def test_out_of_order():
    assert array_diff([1, 2, 1], 1) == 2


def test_negative_target():
    assert array_diff([1, 3, 7, 5, 2, 4], -2) == 4
