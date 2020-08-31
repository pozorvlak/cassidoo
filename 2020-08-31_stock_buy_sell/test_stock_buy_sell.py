from hypothesis import given
from hypothesis.strategies import integers, lists

from stock_buy_sell import stock_buy_sell


def intervals(n):
    for i in range(n):
        for j in range(i+1, n):
            yield (i, j)


def stock_buy_sell_quadratic(prices):
    n_days = len(prices)
    buy, sell = max(intervals(n_days), key=lambda xy: prices[xy[1]] - prices[xy[0]])
    return buy + 1, sell + 1


def test_example():
    assert stock_buy_sell([110, 180, 260, 40, 310, 535, 695]) == (4, 7)


@given(lists(integers(), min_size=2))
def test_brute_force(prices):
    sut_buy, sut_sell = stock_buy_sell(prices)
    oracle_buy, oracle_sell = stock_buy_sell_quadratic(prices)
    assert (prices[sut_sell - 1] - prices[sut_buy - 1]
        == prices[oracle_sell - 1] - prices[oracle_buy - 1])


@given(lists(integers(), min_size=2))
def test_sell_after_buy(prices):
    buy, sell = stock_buy_sell(prices)
    assert sell > buy
