"""
Given three numbers, return their product. But, if one of the numbers is the
same as another, it does not count: If two numbers are similar, return the
lonely number. If all numbers are same, return 1.

Example:

$ lonelyNumber(1,2,3)
$ 6

$ lonelyNumber(6,6,4)
$ 4

$ lonelyNumber(7,7,7)
$ 1
"""
from collections import Counter


def lonely_number(x, y, z):
    counts = Counter([x, y, z])
    product = 1
    for i, count in counts.items():
        if count == 1:
            product *= i
    return product


def test_example1():
    assert lonely_number(1,2,3) == 6


def test_example2():
    assert lonely_number(6,6,4) == 4


def test_example3():
    assert lonely_number(7,7,7) == 1
