"""
Given a string containing digits from 2-9, return all possible letter combinations that the number could represent based on phone numbers/letters. For example, 2 could be a, b, or c, 3 could be d, e, or f, and so on.

Example:

$ phoneLetter('9')
$ ['w', 'x', 'y', 'z']

$ phoneLetter('23')
$ ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
"""

from itertools import product
from string import ascii_lowercase

from more_itertools import pairwise


letters = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
}


def phone_letter(number):
    usable_letters = [letters[n] for n in number]
    return [''.join(word) for word in product(*usable_letters)]


def test_example1():
    assert phone_letter('9') == ['w', 'x', 'y', 'z']


def test_example2():
    assert phone_letter('23') == \
            ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']


def test_example3():
    assert phone_letter('2') == ['a', 'b', 'c']
