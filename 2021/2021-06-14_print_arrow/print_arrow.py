"""
Given a direction and a number of columns, write a function that outputs an arrow of asterisks (see the pattern in the examples below)!

Example:

$ printArrow('right', 3)
Output:
*
 *
  *
 *
*

$ printArrow('left', 5)
Output:
    *
   *
  *
 *
*
 *
  *
   *
    *
"""


def line(coord):
    return " " * coord + "*\n"


def print_arrow(direction, n_columns):
    if direction == 'right':
        coords = list(range(n_columns)) + list(reversed(range(n_columns - 1)))
    else:
        coords = list(reversed(range(n_columns))) + list(range(1, n_columns))
    return "".join(line(coord) for coord in coords)


def test_example1():
    assert print_arrow('right', 3) ==  """\
*
 *
  *
 *
*
"""


def test_example2():
    assert print_arrow('left', 5) == """\
    *
   *
  *
 *
*
 *
  *
   *
    *
"""


def test_empty_left():
    assert print_arrow('left', 0) == ""


def test_empty_right():
    assert print_arrow('right', 0) == ""


def test_one_left():
    assert print_arrow('left', 1) == "*\n"


def test_one_right():
    assert print_arrow('right', 1) == "*\n"
