"""
Given a string s and a dictionary of words dict, determine if s can be
segmented into a space-separated sequence of one or more dictionary words.


Example:

> word_break("leetcode", ["leet", "code"])
> true

> word_break("catsandog", ["cat", "cats", "and", "sand", "dog"])
> false
// Although "cat", "cats", "and", and "dog" are in the dictionary, the string
// does not have a valid segmentation where all parts are in the dictionary.

> word_break("aaaaaaaa", ["aa", "aaa"])
> true
// "aaaaaaaa" can be segmented in multiple ways such as "aa aa aa aa" or "aaa
// aa aaa" where "aa" and "aaa" are in the dictionary.
"""

def word_break(s, words):
    if s == "":
        return True
    for w in words:
        if s.startswith(w):
            if word_break(s[len(w):], words):
                return True
    return False


def test_example1():
    assert word_break("leetcode", ["leet", "code"])


def test_example2():
    assert not word_break("catsandog", ["cat", "cats", "and", "sand", "dog"])
    # Although "cat", "cats", "and", and "dog" are in the dictionary, the
    # string does not have a valid segmentation where all parts are in the
    # dictionary.


def test_example3():
    assert word_break("aaaaaaaa", ["aa", "aaa"])
    # "aaaaaaaa" can be segmented in multiple ways such as "aa aa aa aa" or
    # "aaa aa aaa" where "aa" and "aaa" are in the dictionary.
