#!/usr/bin/env python

"""
Given a string that is an HTML-like code snippet, return whether or not the
tags are valid.
"""

import string

def html_validator(s, i=0):
    tag_stack = []
    try:
        while i < len(s):
            if s[i] == '<':
                if s[i + 1] == '/':
                    tag, i = parse_tag(s, i + 2)
                    if tag_stack == [] or tag != tag_stack.pop():
                        # Unmatched close tag
                        return False
                else:
                    tag, i = parse_tag(s, i + 1)
                    if tag is not None:
                        tag_stack.append(tag)
                        print(tag_stack)
            i += 1
    except ValueError:
        return False
    return tag_stack == []


# https://www.w3.org/TR/2011/WD-html5-20110525/syntax.html#syntax-tag-name
tag_chars = set(string.digits + string.ascii_letters)


def parse_tag(s, i):
    tag = ""
    j = i
    while j < len(s) and s[j] in tag_chars:
        tag += s[j].lower()
        j += 1
    while j < len(s) and s[j] != '>':
        j += 1
    if j >= len(s):
        raise ValueError(f"Unclosed tag {tag} at position {i}")
    if s[j - 1] == '/':
        tag = None
    return tag, j
    

def test_example():
    assert html_validator('<tag>I love coding <Component />!</tag>')


def test_unmatched_open_tag():
    assert html_validator('<tag>I love coding') == False


def test_unmatched_close_tag():
    assert html_validator('I love coding</tag>') == False


def test_out_of_order():
    assert html_validator('<i><b></i></b>') == False


def test_unclosed_tag():
    assert html_validator('<i') == False


def test_tag_with_attributes():
    assert html_validator('<foo bar="baz" quux="spoffle"><bar></bar></foo>')


def test_single_tag():
    assert html_validator('<foo><bar /></foo>')
