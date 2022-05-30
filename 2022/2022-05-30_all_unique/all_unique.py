"""
Write a function that determines if all the characters in a given string are
unique. Can you do this without making any new variables? You choose if you
want to include capitalization in your consideration for this one, as a fun
challenge.

Example:

> all_unique('Cassidy')
> false

> all_unique('cat & dog')
> false

> all_unique('cat+dog')
> true
"""
from operator import ne


def all_unique(s, ignore_case=False):
    if ignore_case:
        return all_unique(s.lower(), ignore_case=False)
    return all(map(ne, sorted(s)[:-1], sorted(s)[1:]))


def test_example1():
    assert not all_unique('Cassidy')


def test_example2():
    assert not all_unique('cat & dog')


def test_example3():
    assert all_unique('cat+dog')


def test_example4():
    assert all_unique('Aa') and not all_unique('Aa', ignore_case=True)
