#!/usr/bin/env python

from count_chars import int_to_str


def find_quines():
    for i in range(1, 1000):
        source = f"print('{int_to_str(i)}')"
        if len(source) == i:
            print(f"{i}, {source}")


if __name__ == '__main__':
    find_quines()