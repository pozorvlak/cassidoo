#!/usr/bin/env python

"""
Design a hashmap without using any built-in libraries. You should include the
following functions:

    put(key, value): Insert a (key, value) pair into the hashmap. If the value
      already exists, update the value.
    get(key): Returns the value to which key is mapped, or -1 if this map
      contains nothing for key.
    remove(key): Remove the mapping for the value in key if it exists.
"""

from hypothesis import note
import hypothesis.strategies as st
from hypothesis.stateful import Bundle, RuleBasedStateMachine, rule


class AList:
    def __init__(self):
        self.map = []

    def put(self, key, value):
        self.map.insert(0, (key, value))

    def get(self, key):
        for (k, v) in self.map:
            if k == key:
                return v
        return -1

    def remove(self, key):
        deletions = []
        for i, (k, v) in enumerate(self.map):
            if k == key:
                deletions.append(i)
        for j, i in enumerate(deletions):
            del self.map[i - j]

    def __str__(self):
        return str(self.map)


class HashMap:
    def __init__(self):
        self.size = 0
        self.map = [None]

    def put(self, key, value):
        h = hash(key) % len(self.map)
        if self.map[h] is None:
            self.map[h] = AList()
        self.map[h].put(key, value)

    def get(self, key):
        h = hash(key) % len(self.map)
        alist = self.map[h]
        if alist is None:
            return -1
        assert isinstance(alist, AList)
        return alist.get(key)

    def remove(self, key):
        h = hash(key) % len(self.map)
        alist = self.map[h]
        if alist is not None:
            alist.remove(key)


class HashTableComparison(RuleBasedStateMachine):
    def __init__(self):
        super(HashTableComparison, self).__init__()
        self.hashmap = HashMap()
        self.model = {}

    keys = Bundle("keys")
    values = Bundle("values")

    @rule(target=keys, k=st.binary())
    def add_key(self, k):
        return k

    @rule(target=values, v=st.integers())
    def add_value(self, v):
        return v

    @rule(k=keys, v=values)
    def put(self, k, v):
        self.hashmap.put(k, v)
        self.model[k] = v

    @rule(k=keys)
    def get(self, k):
        assert self.hashmap.get(k) == self.model.get(k, -1)

    @rule(k=keys)
    def remove(self, k):
        self.hashmap.remove(k)
        if k in self.model:
            del self.model[k]


TestModel = HashTableComparison.TestCase
