"""
Given an array of integers, return the index of each local peak in the array. A “peak” element is an element that is greater than its neighbors.


Example:

$ local_peaks([1,2,3,1])
$ [2]

$ local_peaks([1,3,2,3,5,6,4])
$ [1, 5]
"""

from hypothesis import given, strategies as st
import numpy as np


def is_peak(xs, i):
    if len(xs) == 1:
        return True
    if i == 0:
        return xs[0] > xs[1]
    elif i == len(xs) - 1:
        return xs[-1] > xs[-2]
    else:
        return xs[i - 1] < xs[i] and xs[i] > xs[i + 1]


def oracle(xs):
    return [i for i in range(len(xs)) if is_peak(xs, i)]


def local_peaks(xs):
    if xs == []:
        return []
    xs = np.array(xs)
    higher_than_last = np.concatenate([[True], xs[:-1] < xs[1:]])
    higher_than_next = np.concatenate([xs[:-1] > xs[1:], [True]])
    peaks = higher_than_last & higher_than_next
    print(peaks)
    return np.nonzero(peaks)[0].tolist()


def test_example1():
    assert local_peaks([1,2,3,1]) == [2]


def test_example2():
    assert local_peaks([1,3,2,3,5,6,4]) == [1, 5]


@given(st.lists(st.integers()))
def test_oracle(xs):
    assert oracle(xs) == local_peaks(xs)
