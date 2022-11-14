"""
Given a list of strings arr, and a max size n, return a new list where the strings (from left to right) are joined together with a space, so that each new string is less than or equal to the max size.

Examples:

> combine_strings(["a", "b", "c", "d", "e", "f", "g"], 5)
> ["a b c", "d e f", "g"]

> combine_strings(["a", "b", "c", "d", "e", "f", "g"], 12)
> ["a b c d e f", "g"]

> combine_strings(["alpha", "beta", "gamma", "delta", "epsilon"], 20)
> ["alpha beta gamma", "delta epsilon"]
"""

def _combine_strings(arr, n):
    curr_string = None
    for s in arr:
        if curr_string is None:
            next_string = s
        else:
            next_string = curr_string + " " + s
        if len(next_string) > n:
            yield curr_string
            curr_string = s
        else:
            curr_string = next_string
    yield curr_string


def combine_strings(arr, n):
    return list(_combine_strings(arr, n))


def test_example1():
    assert combine_strings(["a", "b", "c", "d", "e", "f", "g"], 5) \
        == ["a b c", "d e f", "g"]


def test_example2():
    assert combine_strings(["a", "b", "c", "d", "e", "f", "g"], 12) \
        == ["a b c d e f", "g"]


def test_example3():
    assert combine_strings(["alpha", "beta", "gamma", "delta", "epsilon"], 20) \
        == ["alpha beta gamma", "delta epsilon"]
