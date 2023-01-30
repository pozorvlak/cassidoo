"""
Given a positive integer, generate an array in which every element is an array
that goes from 1 to the index of that array.

Example:

> generate_arrays(4)
> [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4]]

> generate_arrays(1)
> [[1]]
"""

def generate_arrays(n):
    return [list(range(1, i + 1)) for i in range(1, n + 1)]


def test_example1():
    assert generate_arrays(4) == [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4]]


def test_example2():
    assert generate_arrays(1) == [[1]]
