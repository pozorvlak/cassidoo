#!/usr/bin/env python

import re

import pytest


num_re = re.compile(r'[+\-]?(\d+\.?\d*|\.\d+)')


def valid_num(s):
    return num_re.fullmatch(s) is not None


valid = ["7", "0011", "+3.14", "4.", "-.9", "-123.456", "-0.1"]
invalid = ["abc", "1a", "e8", "–6", "-+3", "95x54e53.", "."]


@pytest.mark.parametrize("s", valid)
def test_valid(s):
    assert valid_num(s)


@pytest.mark.parametrize("s", invalid)
def test_invalid(s):
    assert not valid_num(s)
