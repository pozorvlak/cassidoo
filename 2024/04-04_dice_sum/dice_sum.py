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

def dice_sum(num_dice, num_sides, target):
    if num_dice == 1:
        return 1 if target <= num_sides else 0
    else:
        return sum(
            dice_sum(num_dice - 1, num_sides, target - i)
            for i in range(1, num_sides + 1)
        )


def test_example1():
     # there is only one die, and one way to get 3
    assert dice_sum(1, 6, 3) == 1


def test_example2():
    # 6 ways to get a sum of 7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1
    assert dice_sum(2, 6, 7) == 6
