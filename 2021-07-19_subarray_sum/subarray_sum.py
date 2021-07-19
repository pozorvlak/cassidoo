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
    m = len(xs)
    prefix_indices = defaultdict(list)
    prefix_indices[0].append(0)
    prefix = 0
    count = 0
    for i in range(m):
        prefix += xs[i]
        prefix_indices[prefix].append(i + 1)
        count += len(prefix_indices[prefix - n])
    print(prefix_indices)
    return count


def get_suffix_indices(xs):
    return suffix_indices


def oracle(xs, n):
    m = len(xs)
    count = 0
    for i in range(m):
        for j in range(i, m + 1):
            if sum(xs[i:j]) == n:
                print(f"oracle: {(i, j + 1)}")
            count += (sum(xs[i:j]) == n)
    return count


def test_example():
    # arr[0...3], arr[1...4], arr[3...4]
    assert subarray_sum([10 , 2, -2, -20, 10], -10) == 3


def test_oracle():
    # arr[0...3], arr[1...4], arr[3...4]
    assert oracle([10 , 2, -2, -20, 10], -10) == 3


@given(st.lists(st.integers()), st.integers())
def test_solution_equals_oracle(xs, n):
    assert subarray_sum(xs, n) == oracle(xs, n)
