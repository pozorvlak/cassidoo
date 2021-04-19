"""
Given an integer array, move all 0s to the end of it while maintaining the
relative order of the non-zeroes. Bonus: do this without making a copy of the
array!

Example:

$ moveZeroes([0,2,0,3,8])
$ [2,3,8,0,0]
"""

from more_itertools import quantify
from hypothesis import given
import hypothesis.strategies as st


def move_zeroes(xs):
    insert = 0
    for i, x in enumerate(xs):
        if x != 0:
            xs[insert] = x
            insert += 1
    for i in range(insert, len(xs)):
        xs[i] = 0
    return xs


def test_example():
    assert move_zeroes([0,2,0,3,8]) == [2,3,8,0,0]


def test_all_zeroes():
    assert move_zeroes([0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0]


def test_no_zeroes():
    assert move_zeroes([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


@given(st.lists(st.integers()))
def test_same_length(xs):
    before = xs.copy()
    assert len(before) == len(move_zeroes(xs))


@given(st.lists(st.integers()))
def test_same_zero_count(xs):
    before_zeroes = quantify(xs, lambda x: x == 0)
    after = move_zeroes(xs)
    after_zeroes = quantify(after, lambda x: x == 0)
    assert before_zeroes == after_zeroes


@given(st.lists(st.integers()))
def zeroes_at_end(xs):
    after = move_zeroes(xs)
    seen_zero = False
    for x in after:
        if x == 0:
            seen_zero = True
        assert not (seen_zero and x != 0)


@given(st.lists(st.integers()))
def same_order_otherwise(xs):
    stripped_before = [x for x in xs if x != 0]
    after = move_zeroes(xs)
    stripped_after = [x for x in after if x != 0]
    assert stripped_before == stripped_after
