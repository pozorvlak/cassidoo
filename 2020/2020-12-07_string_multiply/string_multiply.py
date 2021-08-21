#/usr/bin/env python

"""
Given two non-negative integers n1 and n2 represented as strings, return the product of n1 and n2, also represented as a string. Neither input will start with 0, and don’t just convert it to an integer and do the math that way.

Examples:

$ stringMultiply(“123”, “456”)
$ “56088”
"""

from hypothesis import given
import hypothesis.strategies as st


times = { (str(a), str(b)): a * b for a in range(10) for b in range(10) }
add = { (str(a), str(b)): a + b for a in range(10) for b in range(10) }


def string_multiply(x, y):
    result = 0
    x_place = 1
    for xc in x[::-1]:
        col_result = 0
        y_place = 1
        for yc in y[::-1]:
            col_result += times[(xc, yc)] * y_place
            y_place *= 10
        result += col_result * x_place
        x_place *= 10
    return str(result)


def test_example():
    assert string_multiply("123", "456") == "56088"


@given(st.integers(min_value=1), st.integers(min_value=1))
def test_oracle(x, y):
    assert string_multiply(str(x), str(y)) == str(x * y)
