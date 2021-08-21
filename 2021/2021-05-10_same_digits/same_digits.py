"""
Given an integer n, return true if n^3 and n have the same set of digits.

Example:

$ sameDigits(1) // true
$ sameDigits(10) // true
$ sameDigits(251894) // true
$ sameDigits(251895) // false
"""

def digits(n):
    return set(str(n))


def same_digits(n):
    return digits(n) == digits(n ** 3)


def test_examples():
    assert same_digits(1) == True
    assert same_digits(10) == True
    assert same_digits(251894) == True
    assert same_digits(251895) == False

