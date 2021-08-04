"""
Given a 3x3, 2D array of integers, where every digit is between 0 and 9, except
7, find the minimum number of digits that must be replaced with 7s so that the
sums of the numbers in each row and each column are the same.

Example:

$ missingSevens([[9,4,3],[3,4,9],[4,8,4]])
$ 0

$ missingSevens([[1,5,2],[5,9,5],[6,5,3]])
$ 4

$ missingSevens([[3,9,6],[8,5,5],[8,4,0]])
$ 2
"""

from copy import deepcopy


def bitstrings(n, ones, prefix=[]):
    if n == 0:
        yield prefix
        return
    if ones > 0:
        if ones == n:
            yield prefix + ([1] * ones)
            return
        yield from bitstrings(n - 1, ones - 1, prefix + [1])
    yield from bitstrings(n - 1, ones, prefix + [0])


def reshape(xss):
    return [xss[3*i:3*i+3] for i in range(3)]


def is_latin(matrix):
    row_sums = {sum(row) for row in matrix}
    col_sums = {sum(row[i] for row in matrix) for i in range(3)}
    sums = row_sums | col_sums
    return len(sums) == 1


def missing_sevens(matrix):
    for num_sevens in range(10):
        for bs in bitstrings(9, num_sevens):
            mask = reshape(bs)
            altered = deepcopy(matrix)
            for i in range(3):
                for j in range(3):
                    if mask[i][j]:
                        altered[i][j] = 7
            if is_latin(altered):
                return num_sevens


def test_example1():
    assert missing_sevens([[9,4,3],[3,4,9],[4,8,4]]) == 0


def test_example2():
    assert missing_sevens([[1,5,2],[5,9,5],[6,5,3]]) == 4


def test_example3():
    assert missing_sevens([[3,9,6],[8,5,5],[8,4,0]]) == 2
