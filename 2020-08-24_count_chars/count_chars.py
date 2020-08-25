#!/usr/bin/env python

"""Given a string s and a character c, return the number of occurrences of c in s"""

def num_chars(s, char):
    count = 0
    for c in s:
        if c == char:
            count += 1
    return count


if __name__ == '__main__':
    assert num_chars("oh heavens", "h") == 2
