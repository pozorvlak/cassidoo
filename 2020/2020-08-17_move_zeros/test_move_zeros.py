from hypothesis import given
from hypothesis.strategies import lists, integers

from move_zeros import *


def test_example():
    assert move_zeros([1, 2, 0, 1, 0, 0, 3, 6]) == [1, 2, 1, 3, 6, 0, 0, 0]


@given(lists(integers()))
def test_zeros_at_end(xs):
    ys = move_zeros(xs)
    seen_zero = False
    for y in ys:
        if seen_zero:
            assert y == 0
        elif y == 0:
            seen_zero = True


@given(lists(integers()))
def test_inplace_agrees(xs):
    ys = move_zeros(xs)
    move_zeros_inplace(xs)
    assert xs == ys


@given(lists(integers()))
def test_short_agrees(xs):
    ys = move_zeros(xs)
    zs = move_zeros_short(xs)
    assert ys == zs
