"""
Given a string, calculate the score that it would get in a game of Scrabble. For extra credit, try verifying if the string is a valid word, or take into account premium squares!

Scoring and example:

1 point: E, A, I, O, N, R, T, L, S, U
2 points: D, G
3 points: B, C, M, P
4 points: F, H, V, W, Y
5 points: K
8 points: J, X
10 points: Q, Z

> scrabble_score('FIZZBUZZ')
> 49
"""

LETTERS_BY_SCORE = {
    1: 'EAIONRTLSU',
    2: 'DG',
    3: 'BCMP',
    4: 'FHVWY',
    5: 'K',
    8: 'JX',
    10: 'QZ',
}


SCORES = {c: v for v, letters in LETTERS_BY_SCORE.items() for c in letters}


def scrabble_score(word, dls=None, tls=None, dws=0, tws=0):
    if dls is None:
        dls = []
    if tls is None:
        tls = []
    word = word.upper()
    scores = [SCORES[c] for c in word]
    for i in dls:
        scores[i] *= 2
    for i in tls:
        scores[i] *= 3
    word_score = sum(scores)
    word_score *= 2 ** dws
    word_score *= 3 ** tws
    return word_score


def test_example():
    assert scrabble_score('FIZZBUZZ') == 49


def test_dls():
    assert scrabble_score('eggs', dls=[1]) == 8


def test_tls():
    assert scrabble_score('spam', tls=[3]) == 14


def test_dws():
    assert scrabble_score('beans', dws=2) == 28


def test_tws():
    assert scrabble_score('sausages', tws=1) == 27


def test_dls_and_tws():
    assert scrabble_score('blackpudding', dls=[1, 3, 7], tws=2) == 279
