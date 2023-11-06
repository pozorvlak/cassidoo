"""
Given a list of words and a dictionary of letter scores, find the word with the
highest score according to the rules: score = word_length * (sum of letter
scores in the word). If there are multiple words with the same highest score,
return the lexicographically smallest one.

Example:

const word_list = ["apple", "banana", "cherry", "date", "fig"];

const letter_scores = [...Array(26).keys()].reduce((scores, i) => (
    scores[String.fromCharCode(97 + i)] = i + 1, scores), {}
);
// This produces { 'a': 1, 'b': 2, 'c': 3, 'd': 4, ... }

score_word_game(word_list, letter_scores)
// 'cherry'
"""

from string import ascii_lowercase
from functools import partial


def key(letter_scores, word):
    # Rather than maximise score and minimise word in the case of a tie,
    # we minimise (-score, word) and let Python's lexicographic ordering
    # take care of it.
    return (- len(word) - sum(letter_scores[c] for c in word), word)


def score_word_game(word_list, letter_scores):
    return min(word_list, key=partial(key, letter_scores))


def test_example():
    word_list = ["apple", "banana", "cherry", "date", "fig"]
    letter_scores = {c: i + 1 for i, c in enumerate(ascii_lowercase)}
    assert score_word_game(word_list, letter_scores) == "cherry"
