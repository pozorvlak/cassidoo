"""
Given a string str, write a function to determine the longest substring
containing only two unique characters.

[I'm interpreting this as "at most two unique characters", to handle strings
like "" and "aaaaaaaaa".]

Example:

> unique_substr('eceba')
> 3 // "ece"

> unique_substr('ccaabbb')
> 5 // "aabbb"

> unique_substr('abcabcabc')
> 2 // "ab", "bc", or "ca"
"""

from hypothesis import given, strategies as st


def unique_substr(word):
    if len(word) <= 2:
        return len(word)
    current, other = word[0], None
    current_start, pair_start = 0, 0
    best_length = 0
    for i, c in enumerate(word):
        if c != current:
            if other is not None and c != other:
                # Finish the current two-character run
                best_length = max(best_length, i - pair_start)
                pair_start = current_start
            current, other = c, current
            current_start = i
    best_length = max(best_length, len(word) - pair_start)
    return best_length


def oracle(word):
    if len(word) <= 2:
        return len(word)
    best_known = 2
    for i in range(len(word) - 1):
        # no point considering substrings shorter than best_known
        for j in range(i + best_known + 1, len(word) + 1):
            if len(set(word[i:j])) <= 2:
                best_known = j - i
    return best_known


def test_example1():
    assert unique_substr('eceba') ==  3 # "ece"


def test_example2():
    assert unique_substr('ccaabbb') == 5 # "aabbb"


def test_example3():
    assert unique_substr('abcabcabc') == 2 # "ab", "bc", or "ca"


def test_example4():
    assert unique_substr('aab') == 3


@given(word=st.text('abcdefghijklmnopqrstuvwxyz'))
def test_oracle(word):
    assert oracle(word) == unique_substr(word)
