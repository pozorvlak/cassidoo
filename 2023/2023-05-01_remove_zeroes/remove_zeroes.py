"""
Given a non-empty array containing only non-negative integers, return the list
with trailing and leading zeroes removed.

Example:

> remove_zeroes([0, 0, 0, 3, 1, 4, 1, 5, 9, 0, 0, 0, 0])
> [3, 1, 4, 1, 5, 9]

> remove_zeroes([0, 0, 0])
> []

> remove_zeroes([8])
> [8]
"""

def remove_zeroes(xs):
    for i, x in enumerate(xs):
        if x != 0:
            break
    for j, x in enumerate(reversed(xs)):
        if x != 0:
            break
    return xs[i:len(xs) - j]


def test_example1():
    assert remove_zeroes([0, 0, 0, 3, 1, 4, 1, 5, 9, 0, 0, 0, 0]) \
        == [3, 1, 4, 1, 5, 9]


def test_example2():
    assert remove_zeroes([0, 0, 0]) == []


def test_example3():
    assert remove_zeroes([8]) == [8]
