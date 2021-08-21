#!/usr/bin/env python

"""
You’re given a string of characters that are only 2s and 0s. Return the index of the first occurrence of “2020” without using the indexOf (or similar) function, and -1 if it’s not found in the string.

Example:
    $ find2020(‘2220000202220020200’)
    $ 14
"""

def find_2020(s):
    for i in range(len(s)):
        if s[i:i + 4] == '2020':
            return i
    return -1


def test_example():
    assert find_2020('2220000202220020200') == 14


def test_missing():
    assert find_2020('22222222222') == -1
