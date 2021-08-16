"""
Given a string s, return the longest palindromic substring in s.

Example:

$ pSubstring('babad')
$ 'bab' // or 'aba'
"""

from collections import defaultdict
from string import ascii_lowercase

from hypothesis import assume, given, strategies as st


def is_palindrome(s):
    if len(s) <= 1:
        return True
    mid = len(s) // 2
    return s[:mid] == s[-mid:][::-1]


def p_substring(s):
    locations = defaultdict(list)
    for i, c in enumerate(s):
        locations[c].insert(0, i)
    best = ""
    for i, c in enumerate(s):
        for j in locations[c]:
            if j - i < len(best):
                break
            if is_palindrome(s[i:j + 1]):
                best = s[i:j + 1]
                break
    return best


def is_palindrome_oracle(s):
    return s == s[::-1]


def oracle(s):
    best = ""
    for i in range(len(s)):
        for j in range(i + len(best) + 1, len(s) + 1):
            if is_palindrome_oracle(s[i:j]):
                best = s[i:j]
    return best


def test_example():
    assert p_substring("babad") in {"bab", "aba"}


@given(st.text(alphabet=ascii_lowercase))
def test_is_palindrome(s):
    assert is_palindrome(p_substring(s))


@given(st.text(alphabet=ascii_lowercase, min_size=1))
def test_known_answer(s):
    palindrome = s + s[::-1]
    assert p_substring("ABC" + palindrome + "XYZ") == palindrome


@given(st.text(alphabet=ascii_lowercase, min_size=2))
def test_known_answer_odd_length(s):
    palindrome = s + s[-2::-1]
    assert p_substring("ABC" + palindrome + "XYZ") == palindrome


@given(st.text(alphabet=ascii_lowercase))
def test_is_palindrome(s):
    assert is_palindrome(s) == is_palindrome_oracle(s)


@given(st.text(alphabet=ascii_lowercase))
def test_oracle(s):
    assert p_substring(s) == oracle(s)
