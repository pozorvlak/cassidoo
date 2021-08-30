"""
Write a function to find the longest common prefix string in an array of
strings.

Example:

$ longestPrefix(["cranberry","crawfish","crap"])
$ "cra"

$ longestPrefix(["parrot", "poodle", "fish"])
$ ""
"""

def longest_prefix(words):
    prefix = ""
    for i in range(min(len(word) for word in words)):
        chars = set(word[i] for word in words)
        if len(chars) == 1:
            prefix = prefix + chars.pop()
        else:
            break
    return prefix


def test_example1():
    assert longest_prefix(["cranberry","crawfish","crap"]) == "cra"


def test_example2():
    assert longest_prefix(["parrot", "poodle", "fish"]) == ""
