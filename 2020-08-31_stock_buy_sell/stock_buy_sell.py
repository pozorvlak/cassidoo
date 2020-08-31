#!/usr/bin/env python

def intervals(xs):
    for i, x in enumerate(xs):
        for j, y in enumerate(xs[i+1:]):
            yield (i, i + 1 + j, y - x)

def stock_buy_sell(stock_price):
    buy, sell, profit = max(intervals(stock_price), key=lambda xyz: xyz[2])
    return buy + 1, sell + 1
