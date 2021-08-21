#!/usr/bin/env python

"""
Given a string array representing a tic-tac-toe board, return true if and only
if it’s possible to reach this board position during the course of a valid
tic-tac-toe game. You can assume the first player will always play X first, and
players will only fill in blank spaces. The game will end if there is 3 in a
row, column, or diagonal, or if the board is full.

Example:

$ valid_ttt_position(["XOX", " X ", "   "])
$ false
$ valid_ttt_position(["XOX", "O O", "XOX"])
$ true
$ valid_ttt_position(["OOO", "   ", "XXX"])
$ false
$ valid_ttt_position(["  O", "   ", "   "])
$ false
"""

from collections import Counter

def three_in_a_row(line):
    return line[0] == line[1] == line[2]


def valid_ttt_position(board):
    counts = Counter()
    for line in board:
        counts.update(line)
    if not (0 <= counts.get('X', 0) - counts.get('O', 0) <= 1):
        return False
    completed_lines = 0
    for line in board:
        completed_lines += three_in_a_row(line)
    for j in range(3):
        completed_lines += three_in_a_row([board[i][j] for i in range(3)])
    completed_lines += three_in_a_row([board[i][i] for i in range(3)])
    completed_lines += three_in_a_row([board[i][2 - i] for i in range(3)])
    return completed_lines <= 1


def test_example1():
    assert not valid_ttt_position(["XOX", " X ", "   "])


def test_example2():
    assert valid_ttt_position(["XOX", "O O", "XOX"])


def test_example3():
    assert not valid_ttt_position(["OOO", "   ", "XXX"])


def test_example4():
    assert not valid_ttt_position(["  O", "   ", "   "])

