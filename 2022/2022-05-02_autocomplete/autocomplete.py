"""
Implement a simple version of autocomplete, where given an input string s and a
dictionary of words dict, return the word(s) in dict that partially match s (or
an empty string if nothing matches).

Example:

let dict = ['apple', 'banana', 'cranberry', 'strawberry']

$ simple_autocomplete('app')
$ ['apple']

$ simple_autocomplete('berry')
$ ['cranberry', 'strawberry']

$ simple_autocomplete('fart')
$ []
"""


def simple_autocomplete(words, s):
    return [w for w in words if s in w]


def test_example1():
    d = ['apple', 'banana', 'cranberry', 'strawberry']
    assert simple_autocomplete(d, 'app') == ['apple']


def test_example2():
    d = ['apple', 'banana', 'cranberry', 'strawberry']
    assert simple_autocomplete(d, 'berry') == ['cranberry', 'strawberry']


def test_example3():
    d = ['apple', 'banana', 'cranberry', 'strawberry']
    assert simple_autocomplete(d, 'fart') == []
