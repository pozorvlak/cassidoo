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
from string import ascii_lowercase

from hypothesis import given, strategies as st


def replace_all(pattern, assignments):
    for key, value in assignments.items():
        pattern = pattern.replace(key, value)
    return pattern


def pattern_match(pattern, s):
    uses = Counter(pattern)
    # XXX finish me!
    return False


def oracle(pattern, s):
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


word = st.text(alphabet=ascii_lowercase)


@given(st.text(alphabet="ABCDE", max_size=10), word)
def test_oracle(pattern, s):
    assert oracle(pattern, s) == pattern_match(pattern, s)


@given(st.text(alphabet="ABC", max_size=10), word, word, word)
def test_known_good(pattern, a, b, c):
    s = pattern.replace("A", a).replace("B", b).replace("C", c)
    assert pattern_match(pattern, s)
