#!/usr/bin/env python

from dataclasses import dataclass
from math import ceil


@dataclass
class Order:
    name: str
    num: int


def gimme_pizza(orders, slices_per_pizza):
    return ceil(sum(order.num for order in orders) / slices_per_pizza)


def test_example():
    arr = [Order("Joe", 9), Order("Cami", 3), Order("Cassidy", 4)]
    assert gimme_pizza(arr, 8) == 2 # 2 * 8 = 16 slices needed


def test_wastage():
    arr = [Order("Joe", 9), Order("Cami", 3), Order("Cassidy", 4)]
    assert gimme_pizza(arr, 7) == 3 # 16 \in (2*7, 3*7) slices needed
