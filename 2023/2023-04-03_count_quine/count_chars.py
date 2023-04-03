#!/usr/bin/env python

"""
Write a program that prints the amount of characters its source has in English
words. So a program that is 44 characters long would output “forty four” and a
program that is 108 characters long would output “one hundred eight”.
"""

from sys import argv


UNIT_NAMES = (
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
)

TEEN_NAMES = (
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
)

TEN_NAMES = (
        None,
        None,
        "twenty",
        "thirty",
        "forty",
        "fifty",
        "sixty",
        "seventy",
        "eighty",
        "ninety"
)

GROUP_NAMES = (
        None,
        "thousand",
        "million",
        "billion",
        "trillion",
        "quadrillion"
)


def int_to_str(n):
    if n < 10:
        return UNIT_NAMES[n]
    elif n < 20:
        return TEEN_NAMES[n - 10]
    elif n < 100:
        tens, units = divmod(n, 10)
        ten_name = TEN_NAMES[tens]
        return f"{ten_name}-{UNIT_NAMES[units]}" if units else ten_name
    elif n < 1000:
        hundreds, rest = divmod(n, 100)
        hundred_name = UNIT_NAMES[hundreds]
        if rest:
            rest_name = int_to_str(rest)
            return f"{hundred_name} hundred and {rest_name}"
        else:
            return f"{hundred_name} hundred"
    else:
        groups = []
        while n:
            n, lo = divmod(n, 1000)
            groups.append(lo)
        group_names = []
        for i, g in enumerate(groups):
            if not g:
                continue
            g_name = int_to_str(g)
            if i == 0:
                group_names.append(g_name)
            else:
                group_names.insert(0, f"{g_name} {GROUP_NAMES[i]}")
        return ", ".join(group_names)


if __name__ == '__main__':
    filename = argv[1] if len(argv) > 1 else __file__
    with open(filename) as f:
        contents = f.read()
        print(int_to_str(len(contents)))
