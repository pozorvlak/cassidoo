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

# We only import these libraries for testing!
from hypothesis import note
import hypothesis.strategies as st
from hypothesis.stateful import Bundle, RuleBasedStateMachine, rule


class AList:
    def __init__(self, initial_entries=None):
        self.map = []
        if initial_entries is not None:
            self.map.extend(initial_entries)

    def put(self, key, value):
        for i, (k, v) in enumerate(self.map):
            if k == key:
                self.map[i] = (key, value)
                return 0
        self.map.append((key, value))
        return 1

    def get(self, key):
        for (k, v) in self.map:
            if k == key:
                return v
        return -1

    def remove(self, key):
        for i, (k, v) in enumerate(self.map):
            if k == key:
                del self.map[i]
                return 1
        return 0

    def __repr__(self):
        return f"AList({repr(self.map)})"

    def items(self):
        yield from self.map


class HashMap:
    def __init__(self):
        self.size = 0
        self.map = [None]

    def resize(self):
        old_map = self.map
        self.map = [None] * (2 * len(old_map))
        old_size = self.size
        self.size = 0
        for alist in old_map:
            if alist is not None:
                for key, value in alist.items():
                    self.put(key, value)
        assert self.size == old_size

    def put(self, key, value):
        if self.size == len(self.map):
            self.resize()
        h = hash(key) % len(self.map)
        if self.map[h] is None:
            self.map[h] = AList()
        self.size += self.map[h].put(key, value)

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
            self.size -= alist.remove(key)

    def __len__(self):
        return self.size


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
