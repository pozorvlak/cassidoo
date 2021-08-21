"""
Given an array of 0s and 1s that represent a garden, where 0 is a plot that
hasn’t been planted on, and 1 is a plot that has been planted on, return true
if n plants can be planted without touching another plant.

Example:

garden = [1,0,0,0,1]

$ canPlant(garden, 1)
$ true // plant at position 2
$ canPlant(garden, 4)
$ false // there are only 3 plots, and two of them can't be planted on
"""

def can_plant(garden, count):
    plots = garden.copy()
    can_plant = 0
    for i in range(len(plots)):
        if 1 not in plots[max(0, i-1):min(i+1, len(plots))]:
            plots[i] = 1
            can_plant += 1
            if can_plant >= count:
                return True


def test_example():
    garden = [1,0,0,0,1]
    assert can_plant(garden, 1)
    assert not can_plant(garden, 4)
