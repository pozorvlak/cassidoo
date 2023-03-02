"""
Given a string of parentheses, return the number of parentheses you need to add
to the string in order for it to be balanced.

Examples:

> num_balanced('()')
> 0

> num_balanced('(()')
> 1

> num_balanced('))()))))()')
> 6

> num_balanced(')))))')
> 5
"""

def num_balanced(parens):
    current = 0
    lo = 0
    for p in parens:
        if p == '(':
            current += 1
        elif p == ')':
            current -= 1
            if current < lo:
                lo = current
    print(parens, current, lo)
    if lo < 0:
        # -lo (s to start, then current - lo )s to end
        return current - 2 * lo
    else:
        # current )s to end
        return current


def test_example1():
    assert num_balanced('()') == 0


def test_example2():
    assert num_balanced('(()') == 1


def test_example3():
    assert num_balanced('))()))))()') == 6


def test_example4():
    assert num_balanced(')))))') == 5


def test_example5():
    assert num_balanced(')(') == 2


def test_example6():
    assert num_balanced(')') == 1


def test_example7():
    assert num_balanced('(') == 1
