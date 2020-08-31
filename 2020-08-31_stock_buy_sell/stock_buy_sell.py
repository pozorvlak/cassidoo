#!/usr/bin/env python

def intervals(n):
    for i in range(n):
        for j in range(i+1, n):
            yield (i, j)


def stock_buy_sell(prices):
    n_days = len(prices)
    buy, sell = max(intervals(n_days), key=lambda xy: prices[xy[1]] - prices[xy[0]])
    return buy + 1, sell + 1
