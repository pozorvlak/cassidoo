"""
Given an array of integers, find whether it’s possible to construct an integer
using all the digits of the numbers in the array such that it would be
divisible by n (where n is 1 <= n <= 9). If it’s possible, return true, else
return false.

Example:

> divisible_integers(n=3, arr=[40, 50, 90])
> true // 945000 is divisible by 3
"""

from collections import Counter
from itertools import chain, permutations

from hypothesis import assume, given, strategies as st


def brute_force(n, arr):
    digits = chain.from_iterable(str(i) for i in arr)
    for order in permutations(digits):
        joined = int("".join(order))
        if joined % n == 0:
            print(f"{joined} is divisible by {n}")
            return True
    return False


def contains(haystack, needles):
    return bool(set(haystack) & needles)


def make_multiple_counters(divisor, length):
    multiples = [divisor * n for n in range((10 ** length) // divisor)]
    words = [str(multiple).rjust(length, '0') for multiple in multiples]
    deduped = {"".join(sorted(word)) for word in words}
    return [Counter(int(c) for c in word) for word in deduped]


FOURS = make_multiple_counters(4, 2)
EIGHTS_2 = make_multiple_counters(8, 2)
EIGHTS_3 = make_multiple_counters(8, 3)


def contains_several(haystack, needles):
    counts = Counter(haystack)
    for n in needles:
        if all(counts[c] >= n[c] for c in n):
            return True
    return False


def divisible_integers(n, arr):
    digits = [int(c) for i in arr for c in str(i)]
    if n == 1:
        return True
    elif n == 2:
        return contains(digits, {0, 2, 4, 6, 8})
    elif n == 3:
        return sum(digits) % 3 == 0
    elif n == 4:
        if len(digits) >= 2:
            return contains_several(digits, FOURS)
        else:
            return contains(digits, {0, 4, 8})
    elif n == 5:
        return contains(digits, {0, 5})
    elif n == 6:
        return contains(digits, {0, 2, 4, 6, 8}) and (sum(digits) % 3 == 0)
    elif n == 7:
        return brute_force(7, digits)
    elif n == 8:
        if len(digits) == 1:
            return contains(digits, {0, 8})
        elif len(digits) == 2:
            return contains_several(digits, EIGHTS_2)
        else:
            return contains_several(digits, EIGHTS_3)
    elif n == 9:
        return sum(digits) % 9 == 0


def test_example():
    # 945000 is divisible by 3
    assert divisible_integers(n=3, arr=[40, 50, 90])


@given(
    n=st.integers(min_value=1, max_value=9),
    arr=st.lists(st.integers(min_value=0, max_value=100),
                 min_size=1, max_size=4)
)
def test_oracle(n, arr):
    assume(n != 7)  # This case isn't worth testing since we call brute_force
    assert divisible_integers(n, arr) == brute_force(n, arr)
