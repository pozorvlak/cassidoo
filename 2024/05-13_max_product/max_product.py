"""
Write a function that takes in a list (of length >= 3) of numbers, and returns
the maximum product that can be obtained by multiplying any three integers from
the list.

Example:

> max_product([2, 4, 1, 3, -5, 6])
> 72 // 4*3*6
"""

from heapq import nlargest, nsmallest
from itertools import combinations
from math import prod

from hypothesis import given, strategies as st


def max_product(ints):
    z, y, x = nlargest(3, ints) # in largest-first order
    a, b = nsmallest(2, ints)   # in smallest-first order
    return max(a * b * z, x * y * z) # remember z might be negative


def test_example1():
    assert max_product([2, 4, 1, 3, -5, 6]) == 72 # 4 * 3 * 6


def test_negatives():
    assert max_product([-5, -4, -3, -2, -1]) == -6


def test_zero():
    assert max_product([-3, -2, -1, 0]) == 0


def test_mixed():
    assert max_product([-4, -3, -2, -1, 0, 1, 2, 3]) == 36


def oracle(ints):
    return max(prod(triple) for triple in combinations(ints, 3))


@given(ints=st.lists(st.integers(min_value=-100, max_value=100), min_size=3,
                     max_size=10))
def test_oracle(ints):
    assert oracle(ints) == max_product(ints)
