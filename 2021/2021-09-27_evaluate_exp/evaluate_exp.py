"""
Given a string expression with the symbols T for true, F for false, & for AND,
| for OR, and ^ for XOR, count the number of ways we can parenthesize the
expression so that its value evaluates to true.

Example:

$ evaluateExp('T|T&F^T')
$ 4 // ((T|T)&(F^T)), (T|(T&(F^T))), (((T|T)&F)^T) and (T|((T&F)^T))
"""

from functools import lru_cache
import operator

from hypothesis import given, strategies as st
import numpy as np
import pytest


ops = {
    "&": operator.and_,
    "|": operator.or_,
    "^": operator.xor
}


def evaluations(s):
    if len(s) == 1:
        if s == "T":
            yield True
        elif s == "F":
            yield False
        else:
            raise ValueError(f"Unrecognised character {c}")
        return
    for i, c in enumerate(s):
        if c in ops:
            lefts = list(evaluations(s[:i]))
            rights = list(evaluations(s[i+1:]))
            yield from (ops[c](l, r) for l in lefts for r in rights)


def oracle(s):
    return sum(evaluations(s))


@lru_cache()
def scores(s):
    if len(s) == 1:
        if s == "T":
            return [0, 1]
        elif s == "F":
            return [1, 0]
        else:
            raise ValueError(f"Unrecognised character {c}")
    counts = [0, 0]
    for i, c in enumerate(s):
        if c in ops:
            l = scores(s[:i])
            r = scores(s[i+1:])
            op = ops[c]
            for x in [0, 1]:
                for y in [0, 1]:
                    counts[op(x, y)] += l[x] * r[y]
    return counts


def evaluate_exp(s):
    return scores(s)[1]


def evaluate_exp2(s):
    # counts[i, j, k] is no. of ways to read s[i:j] as k
    counts = np.zeros((len(s), len(s) + 1, 2))
    for i, c in enumerate(s):
        if c == 'F':
            counts[i, i + 1, 0] = 1
        elif c == 'T':
            counts[i, i + 1, 1] = 1
    for length in range(3, len(s) + 1, 2):
        for i in range(0, len(s) - length + 1, 2):
            j = i + length
            for k in range(i + 1, j, 2):
                op = ops[s[k]]
                for x in [0, 1]:
                    for y in [0, 1]:
                        l = counts[i, k, x]
                        r = counts[k + 1, j, y]
                        counts[i, j, op(x, y)] += l * r
    return counts[0, -1, 1]


@pytest.mark.parametrize("s, expected", [
    # ((T|T)&(F^T)), (T|(T&(F^T))), (((T|T)&F)^T) and (T|((T&F)^T))
    ('T|T&F^T', 4),
    ('T^T&F', 1),
    ('T^F', 1),
    ('T', 1),
    ('F', 0),
])
def test_examples(s, expected):
    assert evaluate_exp(s) == expected


def tree_to_str(tree):
    if isinstance(tree, tuple):
        return tree_to_str(tree[0]) + tree[1] + tree_to_str(tree[2])
    return tree


expr_tree = st.recursive(
    st.sampled_from("TF"),
    lambda children: st.tuples(children, st.sampled_from("&|^"), children),
    max_leaves=10
)


expr = expr_tree.map(tree_to_str)


@given(expr)
def test_oracle(s):
    assert oracle(s) == evaluate_exp(s)


@given(expr)
def test_oracle2(s):
    assert evaluate_exp2(s) == evaluate_exp(s)
