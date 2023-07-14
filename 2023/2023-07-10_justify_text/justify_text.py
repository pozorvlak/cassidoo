"""
Given an array of strings and a max width, format the text such that each line
has exactly maxWidth characters and is fully justified. You can choose how you
want to wrap a word.

Example:

> justify_text(
    ["This", "is", "an", "example", "of", "text", "justification."], 16
)
> [
    "This    is    an",
    "example  of text",
    "justification.  "
  ]
"""


def make_line(words, length, linewidth):
    if len(words) == 1:
        return words[0] + (" " * (linewidth - length))
    total_gaps = linewidth - length
    num_gaps = len(words) - 1
    assert total_gaps > num_gaps
    min_gap = total_gaps // num_gaps
    extras = total_gaps % num_gaps
    small_gap = " " * min_gap
    big_gap = " " * (min_gap + 1)
    line = (
        big_gap.join(words[: extras + 1])
        + small_gap
        + small_gap.join(words[extras + 1:])
    )
    assert len(line) == linewidth
    return line


def go(words, linewidth):
    current_line = []
    current_length = 0
    while len(words) > 0:
        word = words.pop(0)
        if len(word) > linewidth:
            yield word[: linewidth - 1] + "-"
            words.insert(0, word[linewidth - 1:])
            continue
        # TODO handle case where word is wider than line
        word_len = len(word)
        if current_length + word_len + len(current_line) - 1 > linewidth:
            yield make_line(current_line, current_length, linewidth)
            current_line = [word]
            current_length = word_len
        else:
            current_line.append(word)
            current_length += word_len
    if current_line:
        yield make_line(current_line, current_length, linewidth)


def justify_text(words, linewidth):
    return list(go(words, linewidth))


def test_example():
    assert justify_text(
        ["This", "is", "an", "example", "of", "text", "justification."], 16
    ) == ["This    is    an", "example  of text", "justification.  "]


def test_hyphenation():
    assert justify_text(["pseudoantidisestablishmentarianism"], 5) == [
        "pseu-",
        "doan-",
        "tidi-",
        "sest-",
        "abli-",
        "shme-",
        "ntar-",
        "iani-",
        "sm   ",
    ]


if __name__ == '__main__':
    test_example()
    test_hyphenation()
