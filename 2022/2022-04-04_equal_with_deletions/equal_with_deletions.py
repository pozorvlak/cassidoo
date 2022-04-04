"""
Given two strings n and m, return true if they are equal when both are entered
into text editors. But: a # means a backspace character (deleting backwards),
and a % means a delete character (deleting forwards).

Example:

> equal_with_deletions("a##x", "#a#x")
> true      // both strings become "x"

> equal_with_deletions("fi##f%%%th %%year #time###", "fifth year time")
> false     // the first string becomes "fart"
"""


def apply_deletions(s):
    result = []
    del_count = 0
    for c in s:
        if c == '#':
            if len(result) > 0:
                result.pop()
        elif c == '%':
            del_count += 1
        elif del_count > 0:
            del_count -= 1
        else:
            result.append(c)
    return "".join(result)


def equal_with_deletions(x, y):
    return apply_deletions(x) == apply_deletions(y)


def test_example_1a():
    assert equal_with_deletions("a##x", "#a#x")  # both strings become "x"


def test_example_1b():
    assert equal_with_deletions("a##x", "x")


def test_example_1c():
    assert equal_with_deletions("#a#x", "x")


def test_example_2a():
    assert not equal_with_deletions(
            "fi##f%%%th %%year #time###",
            "fifth year time")


def test_example_2b():
    assert equal_with_deletions("fi##f%%%th %%year #time###", "fart")
