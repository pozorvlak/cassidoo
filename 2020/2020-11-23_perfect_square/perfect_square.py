#!/usr/bin/env python
"""
Given a positive integer n, write a function that returns true if it is a
perfect square and false otherwise. Don’t use any built-in math functions like
sqrt. Hint: Use binary search!

Examples:

$ perfectSquare(25)
$ true

$ perfectSquare(10) $ false 
"""

from hypothesis import given
import hypothesis.strategies as st

def perfect_square(n: int):
    assert n > 0
    lo = 1
    while 4 * lo * lo < n:
        lo *= 2
    # lo is now the highest power of 2 strictly less than sqrt(n)
    hi = lo
    while hi * hi < n:
        hi *= 2
    # hi is now the lowest power of 2 at least as big as sqrt(n)
    if hi * hi == n:
        return True
    assert lo * lo < n < hi * hi
    while hi - lo > 1:
        mid = (lo + hi) // 2
        print(lo, mid, hi)
        midmid = mid * mid
        if midmid < n:
            lo = mid
        elif midmid == n:
            return True
        else:
            hi = mid
    return False


def test_example1():
    assert perfect_square(25) == True


def test_example2():
    assert perfect_square(10) == False


@given(st.integers(1))
def test_squares(n):
    assert perfect_square(n * n) == True


@given(st.integers(1))
def test_squares_plus_one(n):
    assert perfect_square(n * n + 1) == False


@given(st.integers(1))
def test_squares_times_three(n):
    assert perfect_square(n * n * 3) == False
