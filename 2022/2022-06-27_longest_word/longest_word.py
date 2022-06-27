"""
Given a string str and a set of words dict, find the longest word in dict that
is a subsequence of str.

Example:

let str = "abppplee"
let dict = {"able", "ale", "apple", "bale", "kangaroo"}

$ longest_word(str, dict)
$ 'apple'
// "able" and "ale" also work, but are shorter than "apple"
// "bale" has all the right letters, but not in the right order
"""


def longest_word(seq, words):
    """
    Find the longest word in `words` that is a subsequence of `seq`.
    """
    found = set()
    position = {w: 0 for w in words}
    for char in seq:
        new_found = set()
        for word, i in position.items():
            if char == word[i]:
                new_i = i + 1
                if new_i == len(word):
                    new_found.add(word)
                else:
                    position[word] = new_i
        found.update(new_found)
        for word in new_found:
            del position[word]
    return max(found, key=len)


def test_example():
    """Test the provided example"""
    seq = "abppplee"
    words = {"able", "ale", "apple", "bale", "kangaroo"}
    assert longest_word(seq, words) == 'apple'
