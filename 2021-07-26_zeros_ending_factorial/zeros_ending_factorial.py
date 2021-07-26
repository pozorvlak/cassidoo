"""
Given a positive integer n, write a function that finds the number of zeros at
the end of n! in base 10.

Example:

$ zerosEndingFactorial(1)
$ 0

$ zerosEndingFactorial(5)
$ 1

$ zerosEndingFactorial(100)
$ 24
"""

from math import factorial

from hypothesis import given, strategies as st


def zeros_ending_factorial(n):
    # Because 10 = 2*5 and 2 < 5, the answer is the number of factors of 5 in
    # n!. We get k factors of 5 from each m <= n divisible by 5^k.
    p = 5
    count = 0
    while p <= n:
        count += n // p
        p *= 5
    return count


def oracle(n):
    s = str(factorial(n))[::-1]
    count = 0
    for c in s:
        if c == '0':
            count += 1
        else:
            break
    return count


def test_example1():
    assert zeros_ending_factorial(1) == 0


def test_example2():
    assert zeros_ending_factorial(5) == 1


def test_example3():
    assert zeros_ending_factorial(100) == 24


@given(st.integers(min_value=1, max_value=1000))
def test_oracle(n):
    assert zeros_ending_factorial(n) == oracle(n)
