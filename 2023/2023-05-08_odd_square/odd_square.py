"""
Sum the odd-square numbers less than a given integer n.

Example:

> odd_square_sum(1)
> 0

> odd_square_sum(2)
> 1

> odd_square_sum(9)
> 1

> odd_square_sum(10)
> 10

> odd_square_sum(44)
> 35
"""

from math import sqrt


def odd_square_sum(x):
    return sum(n ** 2 for n in range(1, int(sqrt(x)), 2))


def test_example1():
    assert odd_square_sum(1) == 0


def test_example1():
    assert odd_square_sum(2) == 1


def test_example1():
    assert odd_square_sum(9) == 1


def test_example1():
    assert odd_square_sum(10) == 10


def test_example1():
    assert odd_square_sum(44) == 35
