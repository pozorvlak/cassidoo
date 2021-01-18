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

import hypothesis.strategies as st
from hypothesis.stateful import Bundle, RuleBasedStateMachine, rule


class HashMap:
    def __init__(self):
        self.map = {}

    def put(self, key, value):
        self.map[key] = value

    def get(self, key):
        return self.map.get(key, -1)

    def remove(self, key):
        if key in self.map:
            del self.map[key]


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
