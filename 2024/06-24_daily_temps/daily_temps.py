"""
Write a function that takes an array of daily temperatures and returns an array
where each element is the number of days you would have to wait until a warmer
temperature. If there is no future day for which this is possible, put 0
instead.

Example:

> daily_temperatures([70, 70, 70, 75])
> [3, 2, 1, 0]

> daily_temperatures([90, 80, 70, 60])
> [0, 0, 0, 0]

> daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73])
> [1, 1, 4, 2, 1, 1, 0, 0]
"""

from bisect import bisect_right

from hypothesis import given, strategies as st


def daily_temperatures(temps):
    seen = []
    indices = []
    output = [None for t in temps]
    for i in range(len(temps) - 1, -1, -1):
        t = temps[i]
        # Find the next strictly larger temperature among those we've seen
        j = bisect_right(seen, t)
        if j >= len(seen):
            output[i] = 0
        else:
            output[i] = indices[j] - i
        # Drop all seen values <= t, they're now dominated by t
        seen = [t] + seen[j:]
        indices = [i] + indices[j:]
    return output


def oracle(temps):
    output = [0 for t in temps]
    for i, t1 in enumerate(temps):
        for j, t2 in enumerate(temps[i:]):
            # We check t1 against itself, but this is harmless and
            # avoids an off-by-one error
            if t2 > t1:
                output[i] = j
                break
    return output


def test_example1():
    assert daily_temperatures([70, 70, 70, 75]) == [3, 2, 1, 0]


def test_example2():
    assert daily_temperatures([90, 80, 70, 60]) == [0, 0, 0, 0]


def test_example3():
    assert daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) \
            == [1, 1, 4, 2, 1, 1, 0, 0]


@given(st.lists(st.integers(), max_size=10))
def test_oracle(temps):
    assert daily_temperatures(temps) == oracle(temps)
