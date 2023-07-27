"""
Given an array where each element is the price of a given stock on that index's
day, choose a single day to buy a stock and a different day (in the
future/later in the array) to sell the stock to maximize your profit. Return
the maximum profit that you can get from a given input. If you can't profit,
return 0.

Example:

> maximum_profit([7,1,5,3,6,4])
> 5 // Buy on day 2, and sell on day 5, your profit = 6-1 = 5.
"""


def maximum_profit(prices):
    if prices == []:
        return 0
    lo = prices[0]
    lowest_before = []
    for p in prices:
        lowest_before.append(lo)
        if p < lo:
            lo = p
    return max(sell - buy for (sell, buy) in zip(prices, lowest_before))


def test_example():
    # Buy on day 2, and sell on day 5, your profit = 6-1 = 5.
    assert maximum_profit([7, 1, 5, 3, 6, 4]) == 5
