"""
Write a function that takes in a number from 1 to 1000 and returns that number
in Roman Numerals.
"""

import pytest


BASE_NUMERALS = { 1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M" }

def roman(n):
    retval = ""
    places = sorted(BASE_NUMERALS.keys())
    numerals = BASE_NUMERALS.copy()
    for i in range(0, 5, 2):
        lo = places[i]
        for j in [1, 2]:
            hi = places[i + j]
            numerals[hi - lo] = numerals[lo] + numerals[hi]
    for place in sorted(numerals.keys(), reverse=True):
        while n >= place:
            n -= place
            retval += numerals[place]
    return retval


@pytest.mark.parametrize("input,expected", [
    (1, "I"),
    (2, "II"),
    (5, "V"),
    (6, "VI"),
    (9, "IX"),
    (10, "X"),
    (14, "XIV"),
    (30, "XXX"),
    (40, "XL"),
    (100, "C"),
    (500, "D"),
    (1984, "MCMLXXXIV"),
    (1999, "MCMXCIX"),   # MIM is a nonstandard later extension
    (2000, "MM")
])
def test_examples(input, expected):
    assert roman(input) == expected
