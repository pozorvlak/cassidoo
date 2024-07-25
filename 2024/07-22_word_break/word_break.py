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
from functools import lru_cache
import re
from string import ascii_lowercase

from hypothesis import given, strategies as st


# Depending on how the Python regex engine is implemented, this may be doing
# the same thing as oracle() or it could be doing a linear-time DFA match.
# In informal testing it's significantly faster than oracle(), though!
def word_break(s, words):
    r = re.compile("(" + "|".join(words) + ")*")
    return r.fullmatch(s) is not None


def oracle(s, words):
    return _oracle(s, tuple(w for w in words if w))


@lru_cache
def _oracle(s, words):
    if s == "":
        return True
    for w in words:
        if s.startswith(w):
            if _oracle(s[len(w):], words):
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


@given(
    s=st.text(alphabet=ascii_lowercase, max_size=100),
    words=st.lists(st.text(alphabet=ascii_lowercase, max_size=10), max_size=100)
)
def test_oracle(s, words):
       assert word_break(s, words) == oracle(s, words)
