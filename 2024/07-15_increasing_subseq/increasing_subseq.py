"""
Given an integer array nums, return the length of the longest increasing
subsequence.

Example:

> increasing_subsequence([10, 9, 2, 3, 7, 101, 18])
> 4

> increasing_subsequence([4, 4, 4, 4, 3])
> 1
"""

def increasing_subsequence(seq):
    max_length = 0
    current_length = 0
    last = -float("inf")
    for s in seq:
        if s > last:
            current_length += 1
        else:
            if max_length < current_length:
                max_length = current_length
            current_length = 1
        last = s
    # handle case where the longest streak is at the end
    return max(max_length, current_length)


def test_example1():
    assert increasing_subsequence([10, 9, 2, 3, 7, 101, 18]) == 4


def test_example2():
    assert increasing_subsequence([4, 4, 4, 4, 3]) == 1
