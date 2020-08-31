#!/usr/bin/env python

def stock_buy_sell(prices):
    best_lo = prices[0]
    best_lo_idx = 0
    best_hi = prices[1]
    best_hi_idx = 1
    current_lo = best_lo
    current_lo_idx = best_lo_idx
    current_hi = best_hi
    current_hi_idx = best_hi_idx
    for i in range(1, len(prices)):
        if prices[i] > current_hi:
            current_hi = prices[i]
            current_hi_idx = i
            if current_hi - current_lo > best_hi - best_lo:
                best_lo = current_lo
                best_lo_idx = current_lo_idx
                best_hi = current_hi
                best_hi_idx = current_hi_idx
        elif prices[i] < current_lo:
            current_lo = prices[i]
            current_lo_idx = i
            current_hi = prices[i]
            current_hi_idx = i
    return best_lo_idx + 1, best_hi_idx + 1
