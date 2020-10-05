#!/usr/bin/env python

# Given an array that was once sorted in ascending order is rotated at some
# pivot unknown to you beforehand (so [0,2,4,7,9] might become [7,9,0,2,4], for
# example). Find the minimum value in that array in O(n) or less.

def rotated_min(xs):
    return xs[0]


def test_example():
    assert rotated_min([7, 9, 0, 2, 4]) == 0
