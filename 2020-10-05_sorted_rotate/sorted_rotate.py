#!/usr/bin/env python

# Given an array that was once sorted in ascending order is rotated at some
# pivot unknown to you beforehand (so [0,2,4,7,9] might become [7,9,0,2,4], for
# example). Find the minimum value in that array in O(n) or less.

from hypothesis import assume, given
from hypothesis.strategies import data, integers, lists


def rotated_min(xs):
    return xs[0]


def test_example():
    assert rotated_min([7, 9, 0, 2, 4]) == 0


@given(data())
def test_oracle(data):
    xs = data.draw(lists(integers()))
    assume(len(xs) >= 1)
    ordered = sorted(xs)
    pivot = data.draw(integers(min_value=0, max_value=len(xs) - 1))
    rotated = ordered[:pivot] + ordered[pivot:]
    assert rotated_min(rotated) == min(xs)
