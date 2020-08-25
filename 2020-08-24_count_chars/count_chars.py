#!/usr/bin/env python

"""Given a string s and a character c, return the number of occurrences of c in s"""

from more_itertools import quantify

def num_chars(s, char):
    return quantify(s, lambda c: c == char)

if __name__ == '__main__':
    assert num_chars("oh heavens", "h") == 2
