"""
Given an integer array, find all distinct combinations of a given length x
(with repetition allowed).

Example:

$ distinctCombos([1,1,2], 2)
$ [1, 1], [1, 2], [2, 2]

$ distinctCombos([1,2,3,4], 2)
$ [1, 1], [1, 2], [1, 3], [1, 4], [2, 2], [2, 3], [2, 4], [3, 3], [3, 4], [4, 4]
"""

from itertools import combinations_with_replacement

from hypothesis import assume, given, strategies as st


def distinct_combos(xs, n):
    return list(go(sorted(set(xs)), n))


def go(xs, n):
    if n == 0:
        yield []
        return
    for i, x in enumerate(xs):
        for tail in go(xs[i:], n - 1):
            yield [x] + tail


def oracle(xs, n):
    combos = set(combinations_with_replacement(set(xs), n))
    return sorted(sorted(combo) for combo in combos)


def test_example1():
    assert distinct_combos([1, 1, 2], 2) == [[1, 1], [1, 2], [2, 2]]


def test_example2():
    assert distinct_combos([1, 2, 3, 4], 2) == [
        [1, 1],
        [1, 2],
        [1, 3],
        [1, 4],
        [2, 2],
        [2, 3],
        [2, 4],
        [3, 3],
        [3, 4],
        [4, 4],
    ]


@given(st.lists(st.integers(min_value=0), max_size=5), st.integers(min_value=0, max_value=5))
def test_oracle(xs, n):
    assume(n <= len(xs))
    assert distinct_combos(xs, n) == oracle(xs, n)
