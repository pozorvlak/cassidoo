"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example:

$ form_parens(1)
$ ["()"]

$ form_parens(3)
$ ["((()))","(()())","(())()","()(())","()()()"]
"""

from collections import Counter
from functools import lru_cache

from hypothesis import given, strategies as st


@lru_cache(None)
def form_parens(n):
    if n == 0:
        return [""]
    forms = []
    for i in range(n):
        first = [f"({s})" for s in form_parens(i)]
        rest = form_parens(n - i - 1) 
        forms.extend(f + r for f in first for r in rest)
    return forms


def test_example1():
    assert form_parens(1) == ["()"]


def test_example2():
    assert set(form_parens(3)) == {"((()))","(()())","(())()","()(())","()()()"}


@given(st.integers(min_value=0, max_value=10))
def test_all_unique(n):
    ps = form_parens(n)
    assert len(set(ps)) == len(ps)


@given(st.integers(min_value=1, max_value=10))
def test_all_contain_right_number_of_parens(n):
    ps = form_parens(n)
    for p in ps:
        assert Counter(p) == {'(': n, ')': n}


def is_balanced(p):
    depth = 0
    for c in p:
        if c == '(':
            depth += 1
        elif c == ')':
            depth -= 1
        else:
            raise ValueError(f"Illegal character {c} in {p}")
        if depth < 0:
            return False
    return depth == 0


@given(st.integers(min_value=0, max_value=10))
def test_all_balanced(n):
    ps = form_parens(n)
    for p in ps:
        assert is_balanced(p), p
