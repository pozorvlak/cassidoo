#!/usr/bin/env python

"""
Given a n x m binary matrix filled with 0s and 1s, find the largest rectangle containing only 1s and return its area.

Example:

$ matrix =
  [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","0","1","1"],
  ["1","0","0","1","0"]
  ]
$ largestRect(matrix)
$ 4
"""

def largest_rect(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    max_area = 0
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if val == "1":
                max_rows = rows - i
                max_cols = cols - j
                for i2 in range(max_rows):
                    if matrix[i + i2][j] == "0":
                        break
                    for j2 in range(max_cols):
                        if matrix[i + i2][j + j2] == "1":
                            area = (i2 + 1) * (j2 + 1) 
                            if area > max_area:
                                print(f"Found new max area of {area}, from {(i, j)} to {(i+i2, j+j2)}")
                                max_area = area
                        else:
                            max_cols = j2
                            break
    return max_area



def test_example():
    matrix = [
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","0","1","1"],
        ["1","0","0","1","0"]
    ]
    assert largest_rect(matrix) == 4


def test_example2():
    matrix = [
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","0","1","1"],
        ["0","0","0","1","0"]
    ]
    assert largest_rect(matrix) == 4
