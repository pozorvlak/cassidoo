"""
Given an array of people objects (where each person has a name and a number of
pie pieces they’re hungry for) and a number for the number of pieces that the
pie can be cut into, return the number of pies you need to buy.

Example:

> arr = [{ name: Joe, num: 9 }, { name: Cami, num: 3 }, { name: Cassidy, num: 4 }]
> mmm_pie(arr, 8)
> 2 // 16 pieces needed, pies can be cut into 8 pieces, so 2 pies should be bought
"""

from math import ceil


def mmm_pie(people, max_slices):
    slices_required = sum(p['num'] for p in people)
    return int(ceil(slices_required / max_slices))


def test_example():
    arr = [
            { 'name': 'Joe', 'num': 9 },
            { 'name': 'Cami', 'num': 3 },
            { 'name': 'Cassidy', 'num': 4 }
    ]
    # 16 pieces needed, pies can be cut into 8 pieces, so 2 pies should be bought
    assert mmm_pie(arr, 8) == 2
