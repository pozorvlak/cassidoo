"""
Given two integer arrays of size n, return a new array of size n such that n
consists of only unique elements and the sum of all its elements is maximum.

Example:

let arr1 = [7, 4, 10, 0, 1]
let arr2 = [9, 7, 2, 3, 6]

$ maximizedArray(arr1, arr2)
$ [9, 7, 6, 4, 10]
"""
from itertools import chain
from math import inf

from hypothesis import given
import hypothesis.strategies as st


def maximized_array(xs, ys):
    # Very convoluted implementation to match the ordering in the example!
    if len(xs) == 0:
        return []
    retval = [] # We can't start with ys, because it might have duplicates
    min_val = -inf
    desired_length = len(xs)
    for x in chain(ys, xs):
        if x > min_val and x not in retval:
            retval.append(x)
            if len(retval) >= desired_length:
                min_val = min(retval)
            if len(retval) > desired_length:
                retval.remove(min_val)
            print(x, min_val, retval)
    return retval


def sorted_maximized_array(xs, ys):
    n = len(xs)
    return sorted(set(xs) | set(ys))[-n:]


def test_example():
    arr1 = [7, 4, 10, 0, 1]
    arr2 = [9, 7, 2, 3, 6]
    assert maximized_array(arr1, arr2) == [9, 7, 6, 4, 10]


@given(st.lists(st.tuples(st.integers(), st.integers())))
def test_oracle(xys):
    xs = [xy[0] for xy in xys]
    ys = [xy[1] for xy in xys]
    assert sorted(maximized_array(xs, ys)) == sorted_maximized_array(xs, ys)
