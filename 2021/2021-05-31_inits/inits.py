"""
Given a list, return a list of all its prefixes in ascending order of their
length. You’re essentially implementing the inits function in Haskell!

Example:

$ inits([4, 3, 2, 1])
$ [[], [4], [4,3], [4,3,2], [4,3,2,1]]

$ inits([144])
$ [[], [144]]
"""

from hypothesis import given
import hypothesis.strategies as st


def inits(xs):
    return [xs[:i] for i in range(len(xs) + 1)]


# Functional-style inits, because why not
def reverse(xs):
    return list(reversed(xs))


def go(xs):
    yield reverse(xs)
    if len(xs) == 0:
        return
    yield from go(xs[1:])


def inits2(xs):
    return reverse(list(go(reverse(xs))))


# Tail-recursive functional-style inits, because again, why not?
def inits3(xs, prefix=[[]]):
    if len(xs) == 0:
        return prefix
    else:
        new_prefix = prefix + [prefix[-1] + [xs[0]]]
        return inits3(xs[1:], prefix=new_prefix)


def test_example1():
    assert inits([4, 3, 2, 1]) == [[], [4], [4,3], [4,3,2], [4,3,2,1]]


def test_example2():
    assert inits([144]) == [[], [144]]


@given(st.lists(st.integers()))
def test_oracle(xs):
    assert inits(xs) == inits2(xs)


@given(st.lists(st.integers()))
def test_oracle2(xs):
    assert inits(xs) == inits3(xs)
