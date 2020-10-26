#!/usr/bin/env python

"""
Given an integer array arr, sort the integers in arr in ascending order by the number of 1’s in their binary representation and return the sorted array.

Examples:

$ sortBits([0,1,2,3,4,5,6,7,8])
$ [0,1,2,4,8,3,5,6,7]
"""

def sort_bits(xs):
    # bin(x) returns a string like '0b11', so strip off '0b'
    return sorted(xs, key=lambda x: sum(map(int, bin(x)[2:])))


def test_example():
    assert sort_bits([0,1,2,3,4,5,6,7,8]) == [0,1,2,4,8,3,5,6,7]
