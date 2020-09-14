#!/usr/bin/env python
"""
Given an array of increasing integers, find the length of the longest
fibonacci-like subsequence of the array. If one does not exist, return 0. A
sequence is “fibonacci-like” if X_i + X_{i+1} = X_{i+2}.

Example:

$ fibonacciLike([1,3,7,11,12,14,18])
$ 3 // these sequences: [1,11,12], [3,11,14] or [7,11,18]
"""


def fibonacci_like(xs):
    best = 0
    indices = {x: i for i, x in enumerate(xs)}
    for i in range(len(xs) - 2):
        for j in range(i + 1, len(xs) - 1):
            current = 2
            while True:
                k = indices.get(xs[i] + xs[j], None)
                if k is not None:
                    current += 1
                    i, j = j, k
                else:
                    if current > 2 and current > best:
                        best = current
                    break
    return best


def test_example():
    assert fibonacci_like([1, 3, 7, 11, 12, 14, 18]) == 3
