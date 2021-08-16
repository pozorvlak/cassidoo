"""
Given a string s, return the longest palindromic substring in s.

Example:

$ pSubstring('babad')
$ 'bab' // or 'aba'
"""

from string import ascii_lowercase

from hypothesis import assume, given, strategies as st


def is_palindrome(s):
    return s == s[::-1]


def p_substring(s):
    best = ""
    for i in range(len(s)):
        for j in range(i + len(best), len(s)):
            if is_palindrome(s[i:j]):
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
