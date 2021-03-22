#!/usr/bin/env python

"""
You’re given two integer arrays (n and m), and an integer k. Using the digits
from n and m, return the largest number you can of length k.

Example:

n = [3,4,6,5]
m = [9,0,2,5,8,3]
k = 5
$ maxNum(n, m, k)
$ 98653 # I think this is an error?
"""

from heapq import merge

from hypothesis import given
import hypothesis.strategies as st


def max_num(n, m, k):
    digits = merge(sorted(n, reverse=True), sorted(m, reverse=True), reverse=True)
    num = 0
    last = None
    i = 0
    for d in digits:
        if d == last:
            continue
        i += 1
        if i > k:
            break
        last = d
        num = num * 10 + d
    return num


def oracle(n, m, k):
    # Shorter but probably less efficient implementation, for fuzz-testing
    digits = sorted(set(n) | set(m))[-k:]
    return sum([x * 10 ** i for i, x in enumerate(digits)])


def test_example():
    n = [3, 4, 6, 5]
    m = [9, 0, 2, 5, 8, 3]
    k = 5
    assert max_num(n, m, k) == 98654
    assert n == [3, 4, 6, 5]


def test_example2():
    n = [3, 4, 6, 5]
    m = [9, 0, 2, 5, 8, 3]
    k = 1
    assert max_num(n, m, k) == 9
    assert n == [3, 4, 6, 5]


digits = st.integers(min_value=0, max_value=9)


@st.composite
def inputs(draw):
    n = draw(st.lists(digits))
    m = draw(st.lists(digits, min_size=max(0, 1 - len(n))))
    unique_digits = len(set(n) | set(m))
    k = draw(st.integers(min_value=1, max_value=unique_digits))
    return n, m, k


@given(inputs())
def test_oracle(inputs):
    n, m, k = inputs
    assert max_num(n, m, k) == oracle(n, m, k)


@given(inputs())
def test_length_correct(inputs):
    n, m, k = inputs
    assert len(str(max_num(n, m, k))) == k
