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

def daily_temperatures(temps):
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
