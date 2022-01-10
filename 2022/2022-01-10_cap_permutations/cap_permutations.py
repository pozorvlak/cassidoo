"""
Given a string s, you can transform every letter individually to be lowercase
or uppercase. Return a list of all possible permutations you could create from
s.

Example:

$ capPermutations("ab2")
$ ["ab2","aB2","Ab2","AB2"]

$ capPermutations("35p")
$ ["35p","35P"]
"""

from string import ascii_letters


def cap_permutations(s):
    if len(s) == 0:
        return [""]
    tails = cap_permutations(s[1:])
    if s[0] in ascii_letters:
        l = s[0].lower()
        u = s[0].upper()
        return [l + t for t in tails] + [u + t for t in tails]
    else:
        return [s[0] + t for t in tails]


def test_example1():
    assert cap_permutations("ab2") == ["ab2","aB2","Ab2","AB2"]


def test_example1():
    assert cap_permutations("35p") == ["35p","35P"]

