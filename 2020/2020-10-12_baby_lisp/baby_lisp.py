#!/usr/bin/env python

"""
Given a basic Lisp-like string expression, parse it (where the available
functions are add, subtract, multiply, and divide, and they all take in 2
values).

Examples:

$ babyLisp(‘(add 1 2)’)
$ 3
"""

import re

def baby_lisp(sexpr):
    tokens = tokenize(sexpr)
    return parse(tokens, 0)[0]


def tokenize(sexpr):
    lexer = re.compile(r'\(|\)|add|multiply|divide|subtract|\d+')
    tokens = lexer.findall(sexpr)
    return tokens


def parse(tokens, i):
    if tokens[i] == '(':
        return parse_sexpr(tokens, i+1)
    else:
        return int(tokens[i]), i+1


def parse_sexpr(tokens, i):
    op = tokens[i]
    arg1, j = parse(tokens, i+1)
    arg2, k = parse(tokens, j)
    assert tokens[k] == ')', f"Operation {op} at position {i} must take two arguments"
    if op == 'add':
        return arg1 + arg2, k + 1
    elif op == 'subtract':
        return arg1 - arg2, k + 1
    elif op == 'multiply':
        return arg1 * arg2, k + 1
    elif op == 'divide':
        return arg1 / arg2, k + 1
    else:
        raise NotImplementedError(f"Unknown operation {op} at position {i}")

def test_add():
    assert baby_lisp('(add 1 2)') == 3


def test_nested():
    assert baby_lisp('(multiply 4 (add 2 3))') == 20


def test_divide():
    assert baby_lisp('(divide 7 2)') == 3.5
