"""
Given an array of integers, find the length of the longest sub-sequence such
that elements in the sub-sequence are consecutive integers, the consecutive
numbers can be in any order.

Example:

$ longestSubSeq([1, 9, 87, 3, 10, 4, 20, 2, 45])
$ 4 // 1, 3, 4, 2

$ longestSubSeq([36, 41, 56, 35, 91, 33, 34, 92, 43, 37, 42])
$ 5 // 36, 35, 33, 34, 37
"""


from bisect import bisect
from hypothesis import given, strategies as st


def longest_subseq(xs):
    if len(xs) < 2:
        return len(xs)
    x = xs[0]
    los = [x]
    his = [x]
    seen = {x}
    for x in xs[1:]:
        if x in seen:
            continue
        seen.add(x)
        i = bisect(los, x)
        extend_right = (i < len(los)) and (los[i] == x + 1)
        extend_left = (i > 0) and (his[i - 1] == x - 1)
        if extend_left and extend_right:
            los.pop(i)
            his.pop(i - 1)
        elif extend_left:
            his[i-1] = x
        elif extend_right:
            los[i] = x
        else:
            los.insert(i, x)
            his.insert(i, x)
    print(list(zip(los, his)))
    return max(hi - lo + 1 for (hi, lo) in zip(his, los))


def oracle(xs):
    if len(xs) < 2:
        return len(xs)
    xs = sorted(xs)
    max_len = 1
    current_len = 1
    last = xs[0]
    for x in xs[1:]:
        if x == (last + 1):
            current_len += 1
            if current_len > max_len:
                max_len = current_len
        else:
            current_len = 1
        last = x
    return max_len


def test_example1():
    # 1, 3, 4, 2
    assert longest_subseq([1, 9, 87, 3, 10, 4, 20, 2, 45]) == 4


def test_example2():
    # 36, 35, 33, 34, 37
    assert longest_subseq([36, 41, 56, 35, 91, 33, 34, 92, 43, 37, 42]) == 5


@given(st.lists(st.integers()))
def test_oracle(xs):
    assert longest_subseq(xs) == oracle(xs)
