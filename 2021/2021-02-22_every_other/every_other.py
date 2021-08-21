#!/usr/bin/env python

"""
Given a string str containing only the characters x and y, change it into a string such that there are no matching adjacent characters. You’re allowed to delete zero or more characters in the string. Find the minimum number of required deletions.

Example:

$ everyOther(‘xxyxxy’)
$ 2 // str becomes ‘xyxy’

$ everyOther(‘yyyyy’) $ 4 // str becomes ‘y’
"""

def every_other(s):
    count = 0
    x = None
    for y in s:
        count += y == x
        x = y
    return count


def test_example1():
    assert every_other('xxyxxy') == 2 # str becomes ‘xyxy’


def test_example2():
    assert every_other('yyyyy') == 4 # str becomes ‘y’


def test_empty():
    assert every_other('') == 0
