"""
Imagine you have n dice, and each die has m faces on it (so the numbers are
from 1 to m). Write a function where, given an integer target, it returns the
number of possible ways to roll the dice to get the sum of target face up. You
can safely assume m will never be larger than 20 (so you don't have to deal
with mega huge numbers).

Example:

let n = 1;
let m = 6;

$ dice_sum(n,m,3)
$ 1 // there is only one die, and one way to get 3

$ dice_sum(2,m,7)
$ 6 // 6 ways to get a sum of 7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1
"""
from functools import cache
from math import factorial

import numpy as np
from numpy.linalg import matrix_power


def dice_sum_matrix(num_dice, num_sides, target):
    ones = np.ones((target + 1, target + 1), dtype=np.uint)
    matrix = np.triu(ones, 1) - np.triu(ones, num_sides + 1)
    ways = np.zeros(target + 1, dtype=np.uint)
    ways[0] = 1
    if num_dice % 2:
        ways = ways @ matrix
    # At the start of the i'th iteration:
    #  - ways[j] is dice_sum(num_dice % 2 ** (i + 1), num_sides, j)
    #  - matrix[j, k] is the number of ways of outputting k given input j
    #    and 2 ** i dice rolls.
    # Multiplying by `matrix` simulates one more roll, but we save operations
    # by applying 2 ** n rolls at once for n <= log(num_dice).
    # At each stage we square `matrix` and apply the next bit of num_dice.
    while num_dice > 0:
        matrix = matrix @ matrix
        num_dice = num_dice // 2
        if num_dice % 2:
            ways = ways @ matrix
    return ways[-1]


def dice_sum_numpy(num_dice, num_sides, target):
    ones = np.ones((target + 1, target + 1), dtype=np.uint)
    matrix = np.triu(ones, 1) - np.triu(ones, num_sides + 1)
    #  matrix[j, k] is the number of ways of outputting k given input j
    #  and one die roll.
    # Multiplying by `matrix` simulates one more roll.
    return matrix_power(matrix, num_dice)[0, target]


@cache
def dice_sum_recursive(num_dice, num_sides, target):
    if num_dice == 1:
        return 1 if 1 <= target <= num_sides else 0
    else:
        return sum(
            dice_sum_recursive(num_dice - 1, num_sides, target - i)
            for i in range(1, num_sides + 1)
        )

def dice_sum_unordered(num_dice, num_sides, target):
    # Find all the ways of making target with descending scores,
    # then apply the combination formula to find the total count.
    # This is much slower than the other methods!
    return go(num_dice, num_sides, target, factorial(num_dice), 0)


@cache
def go(num_dice, num_sides, target, count, current):
    if num_sides == 0:
        return 0
    if num_dice == 0:
        if target != 0:
            return 0
        return count / factorial(current)
    # What if we take the highest possible score?
    count_if_take = go(num_dice - 1, num_sides, target - num_sides, count, current + 1)
    # What if we don't?
    count_if_not = go(num_dice, num_sides - 1, target, count / factorial(current), 0)
    return count_if_take + count_if_not


def dice_sum(num_dice, num_sides, target):
    # return dice_sum_matrix(num_dice, num_sides, target)
    # return dice_sum_numpy(num_dice, num_sides, target)
    return dice_sum_recursive(num_dice, num_sides, target)
    # return dice_sum_unordered(num_dice, num_sides, target)


def test_example1():
     # there is only one die, and one way to get 3
    assert dice_sum(1, 6, 3) == 1


def test_example2():
    # 6 ways to get a sum of 7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1
    assert dice_sum(2, 6, 7) == 6


def test_example3():
    assert dice_sum(1, 4, 0) == 0


def test_example4():
    assert dice_sum(2, 2, 3) == 2


def test_big_example():
    assert dice_sum(10, 20, 173) == 94028880


def test_bigger_example():
    assert dice_sum(20, 20, 364) == 280495073622225


def test_more_dice_small_sum():
    assert dice_sum(30, 20, 78) == 1322270553236871418400
