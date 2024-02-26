"""
Given a number and a digit to remove from that number, maximize the resulting
number after the digit has been removed and print it. You can choose how you
want to handle a digit not existing in the number.

Example:

> remove_digit(31415926, 1)
> 3415926 // we picked the second 1 in the number.

> remove_digit(1231, 1)
> 231 // 231 > 123
"""

def remove_digit(number, digit):
    s = str(number)
    d = str(digit)
    pos = -1
    shortenings = []
    while True:
        pos = s.find(d, pos + 1)
        if pos == -1:
            break
        elif pos == len(s) - 1:
            print(f"Removing {digit} at {pos} gives {s[:pos]}")
            shortenings.append(int(s[:pos]))
        else:
            print(f"Removing {digit} at {pos} gives {s[:pos] + s[pos+1:]}")
            shortenings.append(int(s[:pos] + s[pos + 1:]))
    if shortenings == []:
        raise ValueError(f"{digit} not found in {number}")
    return max(shortenings)


def test_example1():
    assert remove_digit(31415926, 1) == 3415926
    # we kept the second 1 in the number.


def test_example2():
    assert remove_digit(1231, 1) == 231 # 231 > 123
