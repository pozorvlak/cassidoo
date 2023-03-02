"""
Given a list of numbers, return all groups of repeating consecutive numbers.

Examples:

> repeated_groups([1, 2, 2, 4, 5])
[[2, 2]]

> repeated_groups([1, 1, 0, 0, 8, 4, 4, 4, 3, 2, 1, 9, 9])
[[1, 1], [0, 0], [4, 4, 4], [9, 9]]
"""

def go(xs):
    if len(xs) == 0:
        return
    current = xs[0]
    current_count = 1
    for x in xs[1:]:
        if x == current:
            current_count += 1
        else:
            if current_count > 1:
                yield [current] * current_count
            current = x
            current_count = 1
    if current_count > 1:
        yield [current] * current_count


def repeated_groups(xs):
    return list(go(xs))


def test_example1():
    assert repeated_groups([1, 2, 2, 4, 5]) == [[2, 2]]


def test_example2():
    assert repeated_groups([1, 1, 0, 0, 8, 4, 4, 4, 3, 2, 1, 9, 9]) \
            == [[1, 1], [0, 0], [4, 4, 4], [9, 9]]
