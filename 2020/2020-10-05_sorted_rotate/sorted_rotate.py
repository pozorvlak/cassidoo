#!/usr/bin/env python

# Given an array that was once sorted in ascending order is rotated at some
# pivot unknown to you beforehand (so [0,2,4,7,9] might become [7,9,0,2,4], for
# example). Find the minimum value in that array in O(n) or less.

from hypothesis import assume, given, note
from hypothesis.strategies import data, integers, lists


def rotated_min(xs):
    lo, hi = 0, len(xs) - 1
    while xs[lo] > xs[hi]:
        if hi - lo == 1:
            lo = hi
        mid = (lo + hi) // 2
        if xs[lo] > xs[mid]:
            hi = mid
        else:
            lo = mid
    return xs[lo]


def test_example():
    assert rotated_min([7, 9, 0, 2, 4]) == 0


def test_unrotated():
    assert rotated_min([0, 2, 4, 7, 9]) == 0


def test_nonstrict():
    assert rotated_min([3, 1, 1, 2]) == 1


@given(data())
def test_oracle(data):
    xs = data.draw(lists(integers()))
    assume(len(xs) >= 1)
    ordered = sorted(xs)
    pivot = data.draw(integers(min_value=0, max_value=len(xs) - 1))
    rotated = ordered[:pivot] + ordered[pivot:]
    note(f"{ordered}, {pivot}, {rotated}")
    assert rotated_min(rotated) == min(xs)
