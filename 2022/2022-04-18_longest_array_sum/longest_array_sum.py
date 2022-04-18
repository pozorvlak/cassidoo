"""
Given an unsorted array of integers and a number n, find the subarray of length
n that has the largest sum.

Example:

$ largest_subarray_sum([3, 1, 4, 1, 5, 9, 2, 6], 3)
$ [9, 2, 6]
"""


def largest_subarray_sum(xs, n):
    idx = max(range(len(xs)), key=lambda i: sum(xs[i:i+n]))
    return xs[idx:idx+n]


def test_example1():
    xs = [3, 1, 4, 1, 5, 9, 2, 6]
    assert largest_subarray_sum(xs, 3) == [9, 2, 6]
