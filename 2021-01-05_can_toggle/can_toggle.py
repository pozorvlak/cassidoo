#!/usr/bin/env python

"""
You’re trying to build an IoT mesh network. Signals can only travel the maximum
of 5 units. You’re given coordinates for the switch, the light, and the mesh
hubs (which capture and forward signals). Return true if the switch can
successfully toggle the light.

Example:

let network = { switch: [0,1], hub: [[2,1], [2,5]], light: [1,6] }
$ canToggle(network)
$ true
"""


from math import sqrt


def can_toggle(network):
    start = tuple(network['switch'])
    end = tuple(network['light'])
    nodes = [start] + [tuple(n) for n in network['hub']] + [end]
    links = {n1: [n2 for n2 in nodes if dist(n1, n2) <= 5] for n1 in nodes}
    seen = {start}
    boundary = links[start]
    while len(boundary) > 0:
        n = boundary.pop(0)
        if n == end:
            return True
        if n in seen:
            continue
        boundary.extend(links[n])
        seen.add(n)
    return False


def dist(n1, n2):
    return sqrt((n1[0] - n2[0]) ** 2 + (n1[1] - n2[1]) ** 2)


def test_example1():
    network = { 'switch': [0,1], 'hub': [[2,1], [2,5]], 'light': [1,6] }
    assert can_toggle(network)


def test_example2():
    network = {
        'switch': [0, 0],
        'hub': [[2, 0], [0, 2], [5, 5], [7, 3]],
        'light': [7, 5]
    }
    assert not can_toggle(network)
