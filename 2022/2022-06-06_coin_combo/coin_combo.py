"""
Given an int array coins and an int amount, return an array of coins that add
up to amount (and an empty array if it’s an impossible combination).

Example:

let coins = [2,3,5,7]
let amount = 17

$ coin_combo(coins, amount)
$ [3,7,7]

$ coin_combo([2,3,5], 11)
$ [3,3,5]
"""

def coin_combo(coins, amount):
    if len(coins) == 0:
        return []
    last = coins[-1]
    if amount >= last:
        prefix = coin_combo(coins, amount - last)
        if sum(prefix) == amount - last:
            return prefix + [last]
    return coin_combo(coins[:-1], amount)


def test_example1():
    assert coin_combo([2, 3, 5, 7], 17) == [3, 7, 7]


def test_example2():
    assert coin_combo([2, 3, 5], 11) == [3, 3, 5]


def test_impossible():
    assert coin_combo([3, 7], 5) == []
