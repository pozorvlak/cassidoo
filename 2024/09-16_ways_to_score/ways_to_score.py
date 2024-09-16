#!/usr/bin/env python

"""
You are given an integer n representing the total points a team wants to score
in an American football game. You need to determine the number of unique ways
the team can achieve exactly n points using any combination of touchdowns (6
points), field goals (3 points), or safeties (2 points).

Example:

> ways_to_score(5)
> 1

> ways_to_score(12)
> 6

> ways_to_score(6)
> 3
"""

from functools import cache


def ways_to_score(total):
    return _ways_to_score(total, (6, 3, 2))


@cache
def _ways_to_score(total, values):
    v = values[0]
    if len(values) == 1:
        return 1 if total % v == 0 else 0
    else:
        return sum(_ways_to_score(total - v * i, values[1:]) for i in range(1 + total // v))


def test_example1():
    assert ways_to_score(5) == 1


def test_example2():
    assert ways_to_score(12) == 6


def test_example3():
    assert ways_to_score(6) == 3
