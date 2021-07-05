"""
Imagine your users are all typing slightly incorrectly, in that they shifted
their hands one key to the right. Write a function that translates what they
mean to say.

Example:

$ translateShift(';p; epe')
"lol wow"

$ translateShift('vtsmnrttu')
"cranberry"
"""

KEYS = ["qwertyuiop[]","asdfghjkl;'#", "\\zxcvbnm,./", "  "]
MAPPING = {k: v for line in KEYS for (k, v) in zip(line[1:], line)}


def translate_shift(s):
    return "".join([MAPPING[c] for c in s])


def test_example1():
    assert translate_shift(';p; epe') == "lol wow"


def test_example2():
    assert translate_shift('vtsmnrttu') == "cranberry"

