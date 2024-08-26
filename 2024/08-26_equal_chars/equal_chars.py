"""
Given a string s containing letters and digits, return the longest substring of
s where the number of distinct letters is equal to the number of distinct
digits. If there are multiple substrings with the same length, return the one
that appears first.


Example:

> equal_chars("abc12345")
> "abc123"

> equal_chars("a123b4c")
> "" // not possible with this example

> equal_chars("a12bc34")
> "a12bc3"
"""

def equal_chars(string):
    best_len, best_i, best_j = 0, 0, -1
    for i in range(len(string) - 1):
        letters, digits = set(), set()
        for j in range(i, len(string)):
            x = string[j]
            if x.lower() in "abcdefghijklmnopqrstuvwxyz":
                letters.add(x)
                print(f"Found letter {x}, letters now {letters}")
            elif x in "1234567890":
                digits.add(x)
                print(f"Found digit {x}, digits now {digits}")
            if len(letters) == len(digits) and (j - i + 1) > best_len:
                print(f"New best string {string[i:j+1]}! {letters} {digits}")
                best_len, best_i, best_j = j - i + 1, i, j
    return string[best_i:best_j+1]


def test_example1():
    assert equal_chars("abc12345") == "abc123"


def test_example2():
    assert equal_chars("a123b4c") == "3b4c"


def test_example3():
    assert equal_chars("a12bc34") == "a12bc3"


def test_example4():
    assert equal_chars("lettersonly") == "" # not possible with this example
