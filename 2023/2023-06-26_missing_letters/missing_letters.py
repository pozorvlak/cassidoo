"""
Write a function that takes an array of consecutive, increasing letters as
input, and returns any missing letters in the array between the first and last
letter.

Example:

> missing_letters(['a','b','c','d','f'])
> ['e']

> missing_letters(['a','b','c','d','e','h','i','j','k','l','m','n','o','p','q','r','s','t','u','w','x','y','z'])
> ['f','g','v']
"""

def missing_letters(xs):
    if xs == []:
        return
    return list(go(xs))


def go(xs):
    curr_ord = ord(xs[0])
    for x in xs[1:]:
        new_ord = ord(x)
        if new_ord - curr_ord > 1:
            yield from [chr(i) for i in range(curr_ord + 1, new_ord)]
        curr_ord = new_ord


def test_example1():
    assert missing_letters('abcdf') == ['e']


def test_example1():
    assert missing_letters('abcdehijklmnopqrstuwxyz') == ['f', 'g', 'v']
