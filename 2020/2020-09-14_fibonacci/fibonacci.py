#!/usr/bin/env python
"""
Given an array of increasing integers, find the length of the longest
fibonacci-like subsequence of the array. If one does not exist, return 0. A
sequence is “fibonacci-like” if X_i + X_{i+1} = X_{i+2}.

Example:

$ fibonacciLike([1,3,7,11,12,14,18])
$ 3 // these sequences: [1,11,12], [3,11,14] or [7,11,18]
"""

from itertools import combinations


def fibonacci_like(xs):
    best = 0
    seen = set(xs)
    for x, y in combinations(xs[:-1], 2):
        current = 2
        while x + y in seen:
            current += 1
            x, y = y, x + y
        if current > 2 and current > best:
            best = current
    return best


def test_example():
    assert fibonacci_like([1, 3, 7, 11, 12, 14, 18]) == 3


def test_fibonacci():
    assert fibonacci_like([1, 1, 2, 3, 5, 8]) == 6
