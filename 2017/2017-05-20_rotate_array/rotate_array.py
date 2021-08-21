"""
Implement a function rotateArray(int[] arr, n) which rotates an array by n places.

Example: [1, 2, 3, 4, 5] rotated by 2 gives [4, 5, 1, 2, 3].
"""

from hypothesis import given, strategies as st

def rotate_array(xs, n):
    if len(xs) == 0:
        return xs
    n %= len(xs)
    return xs[-n:] + xs[:-n]


def test_example():
    assert rotate_array([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]


@given(st.lists(st.integers()))
def test_zero_does_nothing(xs):
    assert rotate_array(xs, 0) == xs


@given(st.lists(st.integers()), st.integers(), st.integers())
def test_sum(xs, n, m):
    assert rotate_array(rotate_array(xs, n), m) == rotate_array(xs, n + m)
