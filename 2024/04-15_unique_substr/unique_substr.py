"""
Given a string str, write a function to determine the longest substring containing only two unique characters.

Example:

> unique_substr('eceba')
> 3 // "ece"

> unique_substr('ccaabbb')
> 5 // "aabbb"

> unique_substr('abcabcabc')
> 2 // "ab", "bc", or "ca"
"""


def unique_substr(word):
    best_known = 2
    for i in range(len(word) - 1):
        # no point considering substrings shorter than best_known
        for j in range(i + best_known + 1, len(word) + 1):
            if len(set(word[i:j])) == 2:
                best_known = j - i
    return best_known


def test_example1():
    assert unique_substr('eceba') ==  3 # "ece"


def test_example2():
    assert unique_substr('ccaabbb') == 5 # "aabbb"


def test_example3():
    assert unique_substr('abcabcabc') == 2 # "ab", "bc", or "ca"
