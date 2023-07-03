"""
Given an integer n, return true if it's a perfect square AND when reversed, is
still a perfect square.

Example:

> reversed_squares(9)
> true

> reversed_squares(441)
> true

> reversed_squares(25)
> false
"""
from math import sqrt


def is_square(n):
    s = sqrt(n)
    return s == int(s)


def reverse_number(n):
    return int(str(n)[::-1])


def reversed_squares(n):
    return is_square(n) and is_square(reverse_number(n))


def test_example1():
    assert reversed_squares(9)


def test_example2():
    assert reversed_squares(441)


def test_example3():
    assert not reversed_squares(25)
