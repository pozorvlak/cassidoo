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

from hypothesis import given
import hypothesis.strategies as st


def get_horizontal_streaks(matrix):
    horiz_streaks = []
    for row in matrix:
        streaks = []
        current_streak = 0
        for val in row:
            if val == "1":
                current_streak += 1
            else:
                current_streak = 0
            streaks.append(current_streak)
        horiz_streaks.append(streaks)
    return horiz_streaks


def get_rects(horiz_streaks):
    # (width, height) pairs for each maximal rectangle whose bottom-right
    # corner is at each point of the matrix
    rects = [[[] for col in row] for row in horiz_streaks]
    for i, row in enumerate(horiz_streaks):
        for j, streak in enumerate(row):
            if streak == 0:
                continue
            up = rects[i - 1][j] if i > 0 else []
            streak_height = 1
            for (width, height) in up:
                if width < streak:
                    rects[i][j].append((width, height + 1))
                else:
                    streak_height = max(streak_height, 1 + height)
            rects[i][j].append((streak, streak_height))
    return rects


def largest_rect(matrix):
    horiz_streaks = get_horizontal_streaks(matrix)
    rects = get_rects(horiz_streaks)
    areas = [rect[0] * rect[1] for row in rects for posn in row for rect in posn]
    if len(areas) > 0:
        return max(areas)
    else:
        return 0


def largest_rect_slow(matrix):
    """
    O(n^2 m^2) solution for comparison
    """
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
                                # print(f"Found new max area of {area}, from {(i, j)} to {(i+i2, j+j2)}")
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


def test_wedge():
    matrix = [
        ["0", "0", "1"],
        ["0", "1", "1"],
        ["1", "1", "1"],
        ["0", "1", "1"],
        ["0", "0", "1"]
    ]
    assert largest_rect(matrix) == 6

@st.composite
def zero_one_matrix(draw):
    n = draw(st.integers(min_value=1, max_value=10))
    return draw(
            st.lists(
                st.lists(st.sampled_from("01"), min_size=n, max_size=n),
                min_size=1))


@given(zero_one_matrix())
def test_oracle(matrix):
    assert largest_rect(matrix) == largest_rect_slow(matrix)
