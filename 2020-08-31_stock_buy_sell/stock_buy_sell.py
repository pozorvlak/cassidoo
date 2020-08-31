#!/usr/bin/env python

def stock_buy_sell(prices):
    best_lo = 0
    best_hi = 1
    current_lo = best_lo
    current_hi = best_hi
    for i in range(1, len(prices)):
        if prices[i] > prices[current_hi]:
            current_hi = i
            if (prices[current_hi] - prices[current_lo]
                    > prices[best_hi] - prices[best_lo]):
                best_lo = current_lo
                best_hi = current_hi
        elif prices[i] < prices[current_lo] and i < len(prices) - 1:
            current_lo = i
            current_hi = i + 1
            # You'd think this wouldn't be necessary, but consider [1, 0, 0]
            if (prices[current_hi] - prices[current_lo]
                    > prices[best_hi] - prices[best_lo]):
                best_lo = current_lo
                best_hi = current_hi
    return best_lo + 1, best_hi + 1
