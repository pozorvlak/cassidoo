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
    current = 0
    for i in range(len(xs) - 2):
        if xs[i] + xs[i+1] == xs[i+2]:
            current += 1
            if current > best:
                best = current
        else:
            current = 0
        print(i, xs[i], current)
    return best


def test_example():
    assert fibonacci_like([1,3,7,11,12,14,18]) == 3

