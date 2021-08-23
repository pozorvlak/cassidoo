"""
Given a list of menu items and their prices, and the amount in your wallet, return all combinations of items that you can buy.

Example:

menu = { 'taco' : 1, 'burger' : 2, 'shawarma' : 3 }
wallet = 3
> combo(menu, wallet)
['taco', 'taco', 'taco']
['taco', 'burger']
['shawarma']
"""

from hypothesis import given, strategies as st


def go(menu, wallet):
    if wallet == 0:
        yield []
        return
    if len(menu) == 0:
        return
    dish, cost = menu[0]
    print(f"Considering {dish}, wallet = {wallet}")
    if cost <= wallet:
        for c in go(menu, wallet - cost):
            yield [dish] + c
    yield from go(menu[1:], wallet)


def combo(menu, wallet):
    return list(go(list(menu.items()), wallet))


def test_empty():
    assert combo({}, 0) == [[]]


def test_minimal_example():
    menu = {"taco": 1}
    wallet = 1
    assert combo(menu, wallet) == [["taco"]]


def test_less_minimal_example():
    menu = {"taco": 1}
    wallet = 2
    assert combo(menu, wallet) == [["taco", "taco"]]


def test_even_less_minimal_example():
    menu = {"taco": 1, "burger": 2}
    wallet = 3
    assert combo(menu, wallet) == [["taco", "taco", "taco"], ["taco", "burger"]]


def test_example():
    menu = {"taco": 1, "burger": 2, "shawarma": 3}
    wallet = 3
    assert combo(menu, wallet) == [
        ["taco", "taco", "taco"],
        ["taco", "burger"],
        ["shawarma"],
    ]


@st.composite
def menu(draw):
    return draw(st.dictionaries(st.text(), st.integers(min_value=1, max_value=10), max_size=10))


@given(menu(), st.integers(min_value=0, max_value=20))
def test_dishes_on_the_menu(menu, wallet):
    combos = combo(menu, wallet)
    for c in combos:
        for dish in c:
            assert dish in menu


@given(menu(), st.integers(min_value=0, max_value=20))
def test_all_combos_affordable(menu, wallet):
    combos = combo(menu, wallet)
    for c in combos:
        assert sum(menu[dish] for dish in c) <= wallet
