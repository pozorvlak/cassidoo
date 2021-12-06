"""
You have to order wrapping paper for presents. Given the length, width, and
height of the boxes you need to wrap, return the number of square feet (or
whatever units you want) of wrapping paper you need to order. Extra credit:
allow for other shapes of presents and their dimensions!

Example:

$ wrap(2, 3, 4)
$ 52 square feet
"""

def wrap(x, y, z):
    return 2 * (x * y + y * z + z * x)


def test_example():
    assert wrap(2, 3, 4) == 52
