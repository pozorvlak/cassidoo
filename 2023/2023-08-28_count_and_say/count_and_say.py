"""
Given a sequence of numbers, generate a "count and say" string.

Example:

> count_and_say(112222555)
> "two 1s, then four 2s, then three 5s"

> count_and_say(3333333333)
> "ten 3s"
"""

NAMES = "one two three four five six seven eight nine ten".split(" ")


def block_to_str(block):
    digit, count = block
    return f"{NAMES[count - 1]} {digit}s"


def count_and_say(number):
    string = str(number)
    current_digit = None
    current_count = 0
    blocks = []
    for c in string:
        if c == current_digit:
            current_count += 1
        else:
            blocks.append((current_digit, current_count))
            current_digit = c
            current_count = 1
    blocks.append((current_digit, current_count))
    blocks.pop(0)   # drop (None, 0) from the front
    return ", then ".join([block_to_str(block) for block in blocks])


def test_example1():
    assert count_and_say(112222555) == "two 1s, then four 2s, then three 5s"


def test_example2():
    assert count_and_say(3333333333) == "ten 3s"
