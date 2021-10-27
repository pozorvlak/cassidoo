"""
Given a string s where some of the letters can be “wilds” (denoted by an
underscore _), find the longest palindrome possible from the letters of s in
order, where the wilds can be any character.

Example:

$ longestPalindrome('abcb_cbcbafg')
$ 'abcbccbcba'

$ longestPalindrome('xyzi_iizy')
$ 'yziiiizy'
"""

def is_equal(c, d):
    return c == d or c == '_' or d == '_'


def is_palindrome(s):
    n = len(s)
    return all(is_equal(s[i], s[n - i - 1]) for i in range(n // 2))


def remove_wildcards(s):
    n = len(s)
    return "".join(c if c != "_" else s[n - i - 1] for i, c in enumerate(s))


def longest_palindrome(s):
    max_len = 0
    longest = ""
    for i in range(len(s)):
        for j in range(i + max_len + 1, len(s) + 1):
            if is_palindrome(s[i:j]):
                longest = s[i:j]
                max_len = j - i
    return remove_wildcards(longest)


def test_example1():
    assert longest_palindrome('abcb_cbcbafg') == 'abcbccbcba'


def test_example2():
    assert longest_palindrome('xyzi_iizy') == 'yziiiizy'
