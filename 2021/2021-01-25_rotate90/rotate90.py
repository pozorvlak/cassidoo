#!/usr/bin/env python

"""
Example:

$ rotate90([[1,2,3],[4,5,6],[7,8,9]])
$ [[7,4,1],[8,5,2],[9,6,3]]
"""

from math import ceil, floor

from hypothesis import given
import hypothesis.strategies as st


def rotate90(m):
    n = len(m)
    assert len(m[0]) == n
    for i in range(ceil(n / 2)):
        for j in range(floor(n / 2)):
            a = m[i][j]
            m[i][j] = m[n - j - 1][i]
            m[n - j - 1][i] = m[n - i - 1][n - j - 1]
            m[n - i - 1][n - j - 1] = m[j][n - i - 1]
            m[j][n - i - 1] = a
    return m


def test_example():
    assert rotate90([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3],
    ]


@st.composite
def matrix(draw):
    n = draw(st.integers(min_value=1, max_value=10))
    return draw(
        st.lists(
            st.lists(st.integers(), min_size=n, max_size=n),
            min_size=n, max_size=n
        )
    )


@given(matrix())
def test_rotate_4x_is_identity(m):
    assert rotate90(rotate90(rotate90(rotate90(m)))) == m
