"""
Given a string, separate it into groups of non-space equal characters, sorted.

Example:

> explode_string('Ahh, abracadabra!')
> ['!',',','A','aaaaa','bb','c','d','hh','rr']

> explode_string('\\o/\\o/')
> ['//','\\\\','oo']
"""


from collections import Counter
from string import whitespace


def explode_string(string):
    counts = Counter(string)
    keys = sorted(counts.keys())
    return [c * counts[c] for c in keys if c not in whitespace]


def test_example1():
    assert explode_string("Ahh, abracadabra!") == [
        "!",
        ",",
        "A",
        "aaaaa",
        "bb",
        "c",
        "d",
        "hh",
        "rr",
    ]


def test_example2():
    assert explode_string("\\o/\\o/") == ["//", "\\\\", "oo"]
