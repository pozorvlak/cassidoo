"""
Given a grid size, and a set of mines (in pairs of rows and columns), generate
the Minesweeper grid for that set of mines. You can use asterisks for mines,
and an x for 0!

Example:

let gridSize = 5
let mines = [[1, 3], [3, 5], [2, 4]]

$ generateMinesweeper(gridSize, mines)

xxxxx
11xxx
*21xx
2*21x
12*1x
"""

from textwrap import dedent

from hypothesis import note, given, strategies as st
import numpy as np


def neighbourhood(coord, grid_size):
    coords = np.arange(-1, 2) + coord
    return coords[(0 <= coords) & (coords < grid_size)]


def generate_grid(grid_size, mines):
    grid = np.zeros((grid_size, grid_size), np.int8)
    for mine in mines:
        mine = (mine[1] - 1, mine[0] - 1)
        grid[mine] = 10
        for i in neighbourhood(mine[0], grid_size):
            for j in neighbourhood(mine[1], grid_size):
                grid[i, j] += 1
    return grid


def print_square(square):
    if square == 0:
        return "x"
    if square >= 10:
        return "*"
    return str(square)


def print_grid(grid):
    return "\n".join(
        "".join(print_square(square) for square in row)
        for row in grid
    )


def generate_minesweeper(grid_size, mines):
    grid = generate_grid(grid_size, mines)
    return print_grid(grid)


def test_example():
    actual = generate_minesweeper(5, [[1, 3], [3, 5], [2, 4]])
    expected =  dedent("""
        xxxxx
        11xxx
        *21xx
        2*21x
        12*1x
        """
    ).strip()
    assert actual == expected


@st.composite
def size_and_mines(draw):
    size = draw(st.integers(min_value=1, max_value=10))
    coord = st.integers(min_value=1, max_value=size)
    coords = st.tuples(coord, coord)
    mines = draw(st.sets(coords, max_size=size*2))
    return size, mines


@given(size_and_mines())
def test_count(s_and_m):
    grid_size, mines = s_and_m
    grid = generate_grid(grid_size, mines)
    note(print_grid(grid))
    for i in range(grid_size):
        for j in range(grid_size):
            if (j + 1, i + 1) in mines:
                assert grid[i, j] >= 10
            else:
                nhd = grid[
                    max(i - 1, 0):min(i + 2, grid_size),
                    max(j - 1, 0):min(j + 2, grid_size)
                ]
                mine_count = np.sum(nhd >= 10)
                assert grid[i, j] == mine_count
