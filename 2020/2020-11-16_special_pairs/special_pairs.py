#!/usr/bin/env python

"""
Given an array of integers arr, a pair (n,m) is called “special” if arr[n] ==
arr[m], and n < m. Return the number of special pairs. Hint: Nested for loops
can work for this one, but a hashmap solution will have a better runtime!

Examples:

$ specialPairs([1,2,3,1,1,3])
$ 4 // (0,3), (0,4), (3,4), (2,5)
"""
from collections import defaultdict

def special_pairs(xs):
    seen = defaultdict(int)
    count = 0
    for x in xs:
        count += seen[x]
        seen[x] += 1
    return count


def test_example():
    assert special_pairs([1, 2, 3, 1, 1, 3]) == 4
