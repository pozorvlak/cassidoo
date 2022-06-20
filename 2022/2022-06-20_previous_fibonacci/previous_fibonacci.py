"""
Given a Fibonacci number, give the previous Fibonacci number. If the number
given is not a Fibonacci number, return -1.

Uses formulae from https://r-knott.surrey.ac.uk/Fibonacci/fibFormula.html .
"""

from math import sqrt


def is_square(n):
    "Is n a square number?"
    s = sqrt(n)
    return int(s) == s


def is_fib(n):
    "Is n a Fibonacci number?"
    return n > 0 and (is_square(5 * n * n + 4) or is_square(5 * n * n - 4))


def previous_fibonacci(n):
    "If n is a Fibonacci number return the previous one, else return -1"
    phi = (sqrt(5) + 1) / 2
    if is_fib(n):
        return round(n / phi)
    return -1


def test_example1():
    assert previous_fibonacci(2) == 1


def test_example2():
    assert previous_fibonacci(13) == 8


def test_example3():
    assert previous_fibonacci(12) == -1


def test_oracle_fib():
    x, y = 1, 1
    for i in range(20):
        assert previous_fibonacci(y) == x
        x, y = y, x + y


def test_oracle_all():
    answers = [-1 for i in range(1000)]
    x, y = 1, 1
    while y < 1000:
        answers[y] = x
        x, y = y, x + y
    for i in range(1000):
        assert previous_fibonacci(i) == answers[i], i
