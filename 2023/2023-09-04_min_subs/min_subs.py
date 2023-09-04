"""
Given an array of integers and a number k (where k is guaranteed to be less than the array's length), return a subarray of length k with the minimum possible sum. Maintain the order of the original array!

Example:

> min_subs([1,3,20,4,8,9,11], 3)
> [4,8,9]

> min_subs([4,4,4,4,8], 2)
> [4,4]
"""

def min_subs(xs, length):
    best_sum = sum(xs[:length])
    current_sum = best_sum
    best_i = 0
    for i in range(len(xs) - length):
        current_sum = current_sum - xs[i] + xs[i + length]
        if current_sum < best_sum:
            best_i = i + 1
    return xs[best_i:best_i + length]


def test_example1():
    assert min_subs([1,3,20,4,8,9,11], 3) == [4,8,9]


def test_example2():
    assert min_subs([4,4,4,4,8], 2) == [4,4]
