#!/usr/bin/env python

"""
You are given a snapshot of a queue of stocks that have changing prices coming in from a stream. Remove the outdated stocks from the queue.

Example:

$ snapshot = [
  { sym: ‘GME’, cost: 280 },
  { sym: ‘PYPL’, cost: 234 },
  { sym: ‘AMZN’, cost: 3206 },
  { sym: ‘AMZN’, cost: 3213 },
  { sym: ‘GME’, cost: 325 }
]
$ stockQueue(snapshot)
$ [{ sym: ‘PYPL’, cost: 234 },
   { sym: ‘AMZN’, cost: 3213 },
   { sym: ‘GME’, cost: 325 }]
"""

from hypothesis import given
import hypothesis.strategies as st


def stock_queue(snapshot):
    seen = {}
    output = []
    for i, stock in enumerate(snapshot):
        sym = stock['sym']
        if sym in seen:
            del output[seen[sym]]
        seen[sym] = len(output)
        output.append(stock)
    return output


def test_example():
    snapshot = [
            { 'sym': 'GME', 'cost': 280 },
            { 'sym': 'PYPL', 'cost': 234 },
            { 'sym': 'AMZN', 'cost': 3206 },
            { 'sym': 'AMZN', 'cost': 3213 },
            { 'sym': 'GME', 'cost': 325 }
            ]
    assert stock_queue(snapshot) == [
        { 'sym': 'PYPL', 'cost': 234 },
        { 'sym': 'AMZN', 'cost': 3213 },
        { 'sym': 'GME', 'cost': 325 }]


@st.composite
def stocks(draw):
    sym = draw(st.from_regex(r"[A-Z]{3,4}"))
    cost = draw(st.integers())
    return { 'sym': sym, 'cost': cost }


@given(st.lists(stocks()))
def test_all_present(snapshot):
    expected = { stock['sym'] for stock in snapshot }
    actual = { stock['sym'] for stock in stock_queue(snapshot) }
    assert expected == actual


@given(st.lists(stocks()))
def test_contains_last_prices(snapshot):
    expected = { stock['sym']: stock['cost'] for stock in snapshot }
    for stock in stock_queue(snapshot):
        sym = stock['sym']
        assert expected[sym] == stock['cost']


@given(st.lists(stocks()))
def test_stock_order(snapshot):
    expected = []
    seen = set()
    for stock in reversed(snapshot):
        if stock['sym'] in seen:
            continue
        expected.append(stock)
        seen.add(stock['sym'])
    expected = list(reversed(expected))
    assert expected == stock_queue(snapshot)
