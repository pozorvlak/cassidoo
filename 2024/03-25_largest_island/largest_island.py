"""
Given a 2D array of 0s and 1s, where 0 represents water and 1 represents land, return the size of the largest "island" in the water. Diagonal connections don't count!

Example:

let map = [
[0,1,1,1,0,0,0,1,1],
[0,1,1,1,0,1,0,0,0],
[0,1,0,0,0,0,0,1,0],
[0,0,1,1,0,1,1,1,0],
]

> largestIsland(map)
> 7
"""

import numpy as np

# We model the islands using a disjoint-set forest
# (https://en.wikipedia.org/wiki/Disjoint-set_data_structure), whose amortised
# runtime grows with the *inverse Ackermann function* (which is to say, as near
# constant as makes no odds)

def find(parents, x):
    root = x
    while parents[root] != root:
        root = parents[root]
    while parents[x] != root:
        parent = parents[x]
        parents[x] = root
        x = parent
    return root


def union(parents, sizes, x, y):
    x = find(parents, x)
    y = find(parents, y)
    if x != y:
        # Make the smaller tree a child of the bigger one
        if sizes[x] < sizes[y]:
            x, y = y, x
        parents[y] = x
        sizes[x] = sizes[x] + sizes[y]
    return x


# `map` is a builtin in Python
def largest_island(chart):
    chart = np.array(chart)
    height, width = chart.shape
    parents = np.full((chart.size,), -1)
    sizes = np.zeros((chart.size,), dtype=int)
    for (i, j) in zip(*np.nonzero(chart)):
        up = i > 0 and chart[i-1, j]
        left = j > 0 and chart[i, j-1]
        my_idx = width * i + j
        if up and left:
            parent = union(parents, sizes, width * (i - 1) + j, width * i + j - 1)
        elif up:
            parent = find(parents, width * (i - 1) + j)
        elif left:
            parent = find(parents, width * i + j - 1)
        else:
            parent = my_idx
        parents[my_idx] = parent
        sizes[parent] += 1
    return np.max(sizes)


def test_example():
    chart = [
        [0,1,1,1,0,0,0,1,1],
        [0,1,1,1,0,1,0,0,0],
        [0,1,0,0,0,0,0,1,0],
        [0,0,1,1,0,1,1,1,0],
    ]
    assert largest_island(chart) == 7

if __name__ == '__main__':
    test_example()
