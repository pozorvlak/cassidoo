"""
Given an array of integers, find whether it’s possible to construct an integer
using all the digits of the numbers in the array such that it would be
divisible by n (where n is 1 <= n <= 9). If it’s possible, return true, else
return false.

Example:

> divisible_integers(n=3, arr=[40, 50, 90])
> true // 945000 is divisible by 3
"""

from itertools import chain, permutations

def divisible_integers(n, arr):
    digits = chain.from_iterable(str(i) for i in arr)
    for order in permutations(digits):
        if int("".join(order)) % n == 0:
            return True
    return False


def test_example():
    # 945000 is divisible by 3
    assert divisible_integers(n=3, arr=[40, 50, 90])
