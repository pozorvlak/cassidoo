"""
Spreadsheet programs often use the A1 Reference Style to refer to columns. Given a column name in this style, return its column number.

Examples of column names to their numbers:

A -> 1
B -> 2
C -> 3
// etc
Z -> 26
AA -> 27
AB -> 28
// etc
AAA -> 703
"""

def char_value(char):
    return ord(char) - ord('A') + 1


def spreadsheet_column(name):
    value = 0
    for char in name:
        value = value * 26 + char_value(char)
    return value


def test_examples():
    examples = dict(
        A=1,
        B=2,
        C=3,
        Z=26,
        AA=27,
        AB=28,
        AAA=703,
    )
    for name, value in examples.items():
        assert(spreadsheet_column(name) == value, name)

