#!/usr/bin/env python

"""
Given a string str and a dictionary dict containing a list of non-empty words,
add spaces in str to construct a “sentence” where each word is a valid word in
dict. Return all possible sentences. You are allowed to reuse the words in
dict.

Example:

str = “penpineapplepenapple”
dict = [“apple”, “pen”, “applepen”, “pine”, “pineapple”]

$ makeSentence(str, dict) $ [ “pen pine apple pen apple”, “pen pineapple pen apple”, “pen pine applepen apple” ]
"""

from collections import defaultdict

class Trie:
    def __init__(self):
        self.contents = defaultdict(Trie)

    def add(self, word):
        if len(word) == 0:
            self.contents[""] = True
            return
        self.contents[word[0]].add(word[1:])


def generator(s, words):
    trie = Trie()
    for word in words:
        trie.add(word)
    boundary = [([], 0)]
    while boundary:
        (prefix, start) = boundary.pop(0)
        t = trie
        idx = start
        while idx < len(s):
            if "" in t.contents:
                boundary.append((prefix + [s[start:idx]], idx))
            if s[idx] not in t.contents:
                break
            t = t.contents[s[idx]]
            idx += 1
        if idx == len(s) and "" in t.contents:
            yield prefix + [s[start:idx]]


def make_sentence(s, words):
    return [" ".join(sentence) for sentence in generator(s, words)]


def oracle_generator(s, words):
    if s == "":
        yield []
        return
    for word in words:
        if s.startswith(word):
            for suffix in oracle_generator(s[len(word):], words):
                yield [word] + suffix
    return


def oracle(s, words):
    return [" ".join(sentence) for sentence in oracle_generator(s, words)]


def test_oracle_example():
    s = "penpineapplepenapple"
    words = ["apple", "pen", "applepen", "pine", "pineapple"]
    assert set(oracle(s, words)) == {
        "pen pine apple pen apple",
        "pen pineapple pen apple",
        "pen pine applepen apple" }


def test_example():
    s = "penpineapplepenapple"
    words = ["apple", "pen", "applepen", "pine", "pineapple"]
    assert set(make_sentence(s, words)) == {
        "pen pine apple pen apple",
        "pen pineapple pen apple",
        "pen pine applepen apple" }
