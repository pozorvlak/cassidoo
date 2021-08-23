"""
Write a function where given a pattern string like "ABCCA" and an input string
like "redyellowbluebluered", return true if and only if there's a one to one
mapping of letters in the pattern to substrings of the input.

> pattern_match('ABA', 'keyboardkey')
true
> pattern_match('AA', 'fishyfish')
false
"""

from collections import Counter
import re


def pattern_match(pattern, s):
    regex = pattern
    for i, char in enumerate(Counter(pattern)):
        regex = regex.replace(char, "(.*?)", 1)
        regex = regex.replace(char, f"\\{i + 1}")
    regex += "$"
    m = re.match(regex, s)
    return m is not None


def test_example1():
    assert pattern_match('ABA', 'keyboardkey')


def test_example2():
    assert not pattern_match('AA', 'fishyfish')
