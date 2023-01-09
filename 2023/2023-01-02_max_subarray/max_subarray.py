"""
Given an array of integers arr and an integer n, return a subarray of arr of
length n where the sum is the largest. Make sure you maintain the order of the
original array, and if n is greater than arr.length, you can choose what you
want to return.

Example:

> max_subarray([-4,2,-5,1,2,3,6,-5,1], 4)
> [1,2,3,6]

> max_subarray([1,2,0,5], 2)
> [0,5]
"""

def max_subarray(xs, n):
    curr_sum = sum(xs[:n])
    best_sum = curr_sum
    best_idx = 0
    for i in range(len(xs) - n):
        curr_sum -= xs[i]
        curr_sum += xs[i + n]
        if curr_sum > best_sum:
            best_sum = curr_sum
            best_idx = i + 1
    return xs[best_idx:best_idx + n]


def test_example1():
    assert max_subarray([-4,2,-5,1,2,3,6,-5,1], 4) == [1,2,3,6]


def test_example2():
    assert max_subarray([1,2,0,5], 2) == [0,5]
