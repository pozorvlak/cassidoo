from hypothesis import given
from hypothesis.strategies import integers

from stock_buy_sell import stock_buy_sell


def test_example():
    assert stock_buy_sell([110, 180, 260, 40, 310, 535, 695]) == (4, 7)
