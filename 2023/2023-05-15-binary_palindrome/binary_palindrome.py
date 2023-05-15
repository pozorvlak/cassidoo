"""
Write a function to find out whether the binary representation of a number is palindrome or not.

Example:

> binary_pal(5)
> true

> binary_pal(10)
> false
"""

from hypothesis import given, note, strategies as st


def binary_pal(x):
    binary = bin(x)[2:]
    return binary == binary[::-1]


def test_example1():
    assert binary_pal(5)


def test_example2():
    assert not binary_pal(10)


@given(st.lists(st.integers(min_value=0, max_value=1), min_size=0, max_size=10))
def test_constructed_palindromes(half):
    half.insert(0, 1)   # need to ensure most significant bit is 1
    x = 0
    for bit in half + half[::-1]:
        x *= 2
        x += bit
    note(f"{bin(x), half, half + half[::-1]}")
    assert binary_pal(x)


@given(st.lists(st.integers(min_value=0, max_value=1), min_size=0, max_size=10))
def test_constructed_nonpalindromes(half):
    half.insert(0, 1)   # need to ensure most significant bit is 1
    other_half = [1 - bit for bit in half[::-1]]
    x = 0
    for bit in half + other_half:
        x *= 2
        x += bit
    note(f"{bin(x)}, {half}, {half + other_half}")
    assert not binary_pal(x)
