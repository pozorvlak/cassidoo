"""
Given a file named merry-christmas.txt that has a single integer x in it, write
a script to generate a Christmas tree with asterisks (*) and output it as
happy-holidays.txt. The tree should have a height of x, and if
merry-christmas.txt is empty, the height should be 25 asterisks tall.

Example (you can be flexible with your output, but this might be helpful for
you as a starting point):

// merry-christmas.txt
3

// happy-holidays.txt
  *
 ***
*****
"""
import os.path


INFILE = "merry-christmas.txt"
OUTFILE = "happy-holidays.txt"


def tree(n):
    lines = []
    for i in range(n):
        padding = " " * (n - i - 1)
        leaves = "*" * (2 * i + 1)
        lines.append(padding + leaves + "\n")
    return "".join(lines)


def main():
    if os.path.exists(INFILE):
        with open(INFILE) as f:
            n = int(f.read())
    else:
        n = 25
    with open(OUTFILE, "w") as f:
        f.write(tree(n))


if __name__ == '__main__':
    main()
