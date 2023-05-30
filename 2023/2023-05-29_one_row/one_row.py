"""
Given an array of words, return the words that can be typed using letters of
only one row on a keyboard. For bonus points, include the option for a user to
pick the type of keyboard they are using (ANSI, ISO, etc), and/or give options
for how many/which rows are allowed!

Example:

> one_row(['candy', 'fart', 'pop', 'Zelda', 'flag', 'typewriter'])
> ['pop', 'flag', 'typewriter']
"""

ROWS = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
INDICES = {c: i for i, word in enumerate(ROWS) for c in word}


def is_one_row(word):
    if len(word) == 0:
        return True
    row_index = INDICES[word[0]]
    for c in word[1:]:
        if INDICES[c] != row_index:
            return False
    return True


def one_row(words):
    return [word for word in words if is_one_row(word.lower())]


def test_example():
    assert one_row(['candy', 'fart', 'pop', 'Zelda', 'flag', 'typewriter']) \
            == ['pop', 'flag', 'typewriter']

