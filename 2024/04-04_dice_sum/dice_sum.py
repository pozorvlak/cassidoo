"""
Imagine you have n dice, and each die has m faces on it (so the numbers are from 1 to m). Write a function where, given an integer target, it returns the number of possible ways to roll the dice to get the sum of target face up. You can safely assume m will never be larger than 20 (so you don't have to deal with mega huge numbers).

Example:

let n = 1;
let m = 6;

$ dice_sum(n,m,3)
$ 1 // there is only one die, and one way to get 3

$ dice_sum(2,m,7)
$ 6 // 6 ways to get a sum of 7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1
"""
from functools import cache

import numpy as np


def dice_sum_matrix(num_dice, num_sides, target):
    print(f"num_dice = {num_dice}, num_sides = {num_sides}, target = {target}")
    ones = np.ones((target + 1, target + 1), dtype=int)
    matrix = np.triu(ones, 1) - np.triu(ones, num_sides + 1)
    ways = np.zeros(target + 1, dtype=int)
    ways[0] = 1
    print(f"num_dice = {num_dice}\nways = {ways}\nmatrix =\n{matrix}\n")
    while num_dice > 0:
        if num_dice % 2:
            ways = ways @ matrix
        matrix = matrix @ matrix
        num_dice = num_dice // 2
        print(f"num_dice = {num_dice}\nways = {ways}\nmatrix =\n{matrix}\n")
    return ways[-1]


@cache
def dice_sum_recursive(num_dice, num_sides, target):
    if num_dice == 1:
        return 1 if 1 <= target <= num_sides else 0
    else:
        return sum(
            dice_sum_recursive(num_dice - 1, num_sides, target - i)
            for i in range(1, num_sides + 1)
        )


def dice_sum(num_dice, num_sides, target):
    return dice_sum_recursive(num_dice, num_sides, target)


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
