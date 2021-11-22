"""
Given an array of strings, group the anagrams together in separate arrays. An
anagram is a word or phrase formed by rearranging the letters of another word
or phrase, using all the original letters exactly once.

Example:

$ group_anagrams(["eat", "tea", "ten", "poop", "net", "ate"])
$ [["poop"], ["net", "ten"], ["eat", "tea", "ate"]]
"""

from collections import defaultdict

def group_anagrams(words):
    groups = defaultdict(list)
    for word in words:
        groups["".join(sorted(word))].append(word)
    return {tuple(sorted(group)) for group in groups.values()}


def test_example():
    assert group_anagrams(["eat", "tea", "ten", "poop", "net", "ate"]) \
        == {("poop",), ("net", "ten"), ("ate", "eat", "tea")}
