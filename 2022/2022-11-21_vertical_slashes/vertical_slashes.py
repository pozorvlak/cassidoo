"""
Write a function that takes a string of slashes (\ and /) and returns all of those slashes drawn downwards in a line connecting them.

Example:

$ vertical_slashes('\\\//\/\\')
\
 \
  \
  /
 /
 \
 /
 \
  \
$ vertical_slashes('\\\\')
\
 \
  \
   \
"""

def vertical_slashes(s):
    left_edge = 0
    lines = []
    for c in s:
        if c == "/":
            left_edge -= 1
            if left_edge < 0:
                raise ValueError("Indent has become negative!")
            line = (" ") * left_edge + c + "\n"
        if c == "\\":
            line = (" ") * left_edge + c + "\n"
            left_edge += 1
        lines.append(line)
    return "".join(lines)


def test_example1():
    assert vertical_slashes('\\\\\\//\\/\\\\') == """\
\\
 \\
  \\
  /
 /
 \\
 /
 \\
  \\
"""


def test_example2():
    assert vertical_slashes('\\\\\\\\') == """\
\\
 \\
  \\
   \\
"""
