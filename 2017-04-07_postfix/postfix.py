"""
Write a simple postfix calculator function that takes in a string expression and returns the result.

Example usage:

postfix('5 4 * 6 2 / +')
> 23
"""

import operator

OPS = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }


def postfix(s):
    words = s.split()
    stack = []
    for word in words:
        if word in OPS:
            y = stack.pop()
            x = stack.pop()
            val = OPS[word](x, y)
        else:
            val = float(word)
        stack.append(val)
    return stack[0]


def test_example():
    assert postfix('5 4 * 6 2 / +') == 23
