#!/usr/bin/env python

"""
Given an array of integers representing asteroids in a row, for each asteroid,
the absolute value represents its size, and the sign represents its direction
(positive = right, negative = left). Return the state of the asteroids after
all collisions (assuming they are moving at the same speed). If two asteroids
meet, the smaller one will explode. When they are the same size, they both
explode. Asteroids moving in the same direction will never meet.
"""


def asteroids(sizes):
    return sizes


def test_example():
    assert asteroids([5, 8, -5]) == [5, 8]


def test_all_same_direction():
    assert asteroids([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_equal_size():
    assert asteroids([5, -5]) == []


def test_multiple_annihilation():
    assert asteroids([4, 1, 2, -3]) == [4]
