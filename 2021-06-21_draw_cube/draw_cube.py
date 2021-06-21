"""
Write a function that draws an ASCII art cube of given height x.

Example:

$ drawCube(2)
  +----+
 /    /|
+----+ |
|    | +
|    |/
+----+

$ drawCube(4)
   +--------+
  /        /|
 /        / |
+--------+  |
|        |  |
|        |  +
|        | /
|        |/
+--------+
"""

def horizontal_edge(n):
    return "+" + ("-" * 2 * n) + "+"


def gap(n):
    return " " * n


def draw_cube(n):
    diag_rows = n // 2
    cube = gap(diag_rows + 1) + horizontal_edge(n) + "\n"
    for i in range(diag_rows, 0, -1):
        cube += gap(i) + "/" + gap(2 * n) + "/" + gap(diag_rows - i) + "|\n"
    cube += horizontal_edge(n) + gap(diag_rows) + "|\n"
    for i in range(n - diag_rows - 1):
        cube += "|" + gap(2 * n) + "|" + gap(diag_rows) + "|\n"
    cube += "|" + gap(2 * n) + "|" + gap(diag_rows) + "+\n"
    for i in range(diag_rows, 0, -1):
        cube += "|" + gap(2 * n) + "|" + gap(i - 1) + "/\n"
    cube += horizontal_edge(n)
    cube += "\n"
    return cube


def test_example1():
    assert draw_cube(2) == """\
  +----+
 /    /|
+----+ |
|    | +
|    |/
+----+
"""


def test_example2():
    assert draw_cube(4) == """\
   +--------+
  /        /|
 /        / |
+--------+  |
|        |  |
|        |  +
|        | /
|        |/
+--------+
"""

