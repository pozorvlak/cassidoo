"""
Given a positive or negative real number, round it to the next whole integer
closer to zero. This means if it’s positive, round down, and if it’s negative,
round up. Try to do this in as few characters as possible!

Test cases:

 1.7    =>  1
-2.1    => -2
 500.4  =>  500
-369.5  => -369
 150    =>  150
-350    => -350
"""

import pytest


def r(x):
    return (abs(x) // 1) * [1, -1][x < 0]


@pytest.mark.parametrize("test_input, expected", [
    ( 1.7, 1),
    (-2.1, -2),
    ( 500.4, 500),
    (-369.5, -369),
    ( 150, 150),
    (-350, -350),
    (0, 0)
])
def test_examples(test_input, expected):
    assert r(test_input) == expected

