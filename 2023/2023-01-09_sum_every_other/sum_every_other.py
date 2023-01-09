"""
Given a number, sum every second digit in that number.

Example:

> sum_every_other(548915381)
> 26 // 4+9+5+8

> sum_every_other(10)
> 0

> sum_every_other(1010.11)
> 1 // 0+0+1
"""

def sum_every_other(num):
    return sum(int(x) for x in str(num)[1::2])


def test_example1():
    assert sum_every_other(548915381) == 26 # 4+9+5+8


def test_example2():
    assert sum_every_other(10) == 0


def test_example3():
    assert sum_every_other(1010.11) == 1 # 0+0+1
