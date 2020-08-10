#!/usr/bin/env python

from copy import copy
from sys import argv


def num_arrangements(counts, previous_animal=-1):
    if all(x == 0 for x in counts):
        return 1
    count = 0
    for i, num_animal in enumerate(counts):
        if num_animal > 0 and i != previous_animal:
            new_counts = copy(counts)
            new_counts[i] -= 1
            count += num_arrangements(new_counts, previous_animal=i)
    return count


if __name__ == '__main__':
    print(num_arrangements([int(i) for i in argv[1:]]))
