#!/usr/bin/env python

from copy import copy
from functools import lru_cache
from sys import argv


@lru_cache()
def go(counts, previous_count):
    if all(x == 0 for x in counts):
        return int(previous_count == 0)
    count = 0
    for i, num_animal in enumerate(counts):
        if num_animal > 0:
            new_counts = tuple(sorted(counts[:i] + counts[i + 1 :] + (previous_count,)))
            count += go(new_counts, counts[i] - 1)
    return count


def num_arrangements(counts):
    return sum(
        go(tuple(sorted(counts[:i] + counts[i + 1 :])), count - 1)
        for i, count in enumerate(counts)
        if count > 0
    )


if __name__ == "__main__":
    print(num_arrangements([int(i) for i in argv[1:]]))
