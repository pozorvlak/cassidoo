#!/usr/bin/env python

"""
Given an unsorted array of integers and a number n, find the number of
continuous subarrays having sum exactly equal n. Return -1 if none exist.

Example:

$ subarraySum([10 , 2, -2, -20, 10], -10)
$ 3 // arr[0...3], arr[1...4], arr[3...4]
"""

from collections import defaultdict

from hypothesis import given, strategies as st
from itertools import takewhile


def subarray_sum(xs, n):
    """Find the number of continuous subarrays of xs with sum n"""
    m = len(xs)
    prefix_indices = defaultdict(int)
    prefix_indices[0] = 1   # the empty prefix has sum 0
    prefix = 0
    count = 0
    for i in range(m):
        prefix += xs[i]
        prefix_indices[prefix] += 1
        count += prefix_indices[prefix - n]
    return count if count > 0 else -1


def oracle(xs, n):
    """Naive O(n^2) solution, for testing"""
    m = len(xs)
    count = 0
    for i in range(m):
        for j in range(i, m + 1):
            count += (sum(xs[i:j]) == n)
    return count if count > 0 else -1


def test_example():
    # arr[0...3], arr[1...4], arr[3...4]
    assert subarray_sum([10 , 2, -2, -20, 10], -10) == 3


def test_none_found():
    assert subarray_sum([1, 2, 3, 4, 5, 6], -1) == -1


def test_oracle():
    # arr[0...3], arr[1...4], arr[3...4]
    assert oracle([10 , 2, -2, -20, 10], -10) == 3


@given(st.lists(st.integers()), st.integers())
def test_solution_equals_oracle(xs, n):
    assert subarray_sum(xs, n) == oracle(xs, n)
