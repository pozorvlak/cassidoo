#!/usr/bin/env python

"""
Given a room size, and the square footage a paint can can cover, return how
many cans of paint you need to buy to paint a room. Assume the room has four
walls. If you’d like to expand this, you can add doors, windows, or any other
room features that might make the problem interesting to solve.

Example:

room = { length: 12, width: 10, height: 9 }
canCoverage = 200

$ numberOfCans(room, canCoverage)
$ 2 // (12 * 9 * 2) + (10 * 9 * 2) = 396, so two cans will cover it
"""

from dataclasses import dataclass
from math import ceil

@dataclass
class Room:
    length: float
    width: float
    height: float


def number_of_cans(room, can_coverage):
    area = 2 * room.height * (room.length + room.width)
    return ceil(area / can_coverage)


def test_example():
    room = Room(length=12, width=10, height=9)
    assert number_of_cans(room, 200) == 2

