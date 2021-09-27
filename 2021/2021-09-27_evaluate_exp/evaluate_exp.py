"""
Given a string expression with the symbols T for true, F for false, & for AND,
| for OR, and ^ for XOR, count the number of ways we can parenthesize the
expression so that its value evaluates to true.

Example:

$ evaluateExp('T|T&F^T')
$ 4 // ((T|T)&(F^T)), (T|(T&(F^T))), (((T|T)&F)^T) and (T|((T&F)^T))
"""

import operator
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
            raise ValueError(f"Unrecognised character {c} at position {i}")
        return
    for i, c in enumerate(s):
        if c in ops:
            lefts = list(evaluations(s[:i]))
            rights = list(evaluations(s[i+1:]))
            yield from (ops[c](l, r) for l in lefts for r in rights)


def evaluate_exp(s):
    return sum(evaluations(s))


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
