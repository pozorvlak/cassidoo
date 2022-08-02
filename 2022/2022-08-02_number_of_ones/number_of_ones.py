"""
Given an integer n, count the total number of 1 digits appearing in all
non-negative integers less than or equal to n.

Example:

> number_of_ones(14)
> 7 // 1, 10, 11, 12, 13, 14
"""


def count_ones(n):
    "Count the 1s in a single number"
    count = 0
    for c in str(n):
        if c == '1':
            count += 1
    return count


def number_of_ones(n):
    """
    Given an integer n, count the total number of 1 digits appearing in all
    non-negative integers less than or equal to n.
    """
    return sum(count_ones(i) for i in range(n + 1))


def test_example1():
    """Test from Cassie's email"""
    assert number_of_ones(14) == 7  # 1, 10, 11, 12, 13, 14
