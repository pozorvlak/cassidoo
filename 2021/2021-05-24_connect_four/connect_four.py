#!/usr/bin/env python

"""
Make a 2-player Connect Four game, where the board is 7 units wide, and 6 units
high. Your program should take in user input when a player puts in a piece, and
have functions boardState() (which returns a 2D array of the current state of
the board) and hasWon() which returns which player has won the game (if any).
"""

# Emoji are two characters wide
BOARD = [["  " for i in range(7)] for j in range(6)]
PLAYERS = ["Red", "Yellow"]
TOKENS = "🔴🟡"
winner = None


def boardState():
    for row in BOARD:
        print("".join(row))
    print(" 0 1 2 3 4 5 6")


# Kinda pointless since I'm calculating the winner based on the last move, but
# it was in the brief...
def hasWon():
    return winner


def highest_filled_row(column):
    for i in range(6):
        if BOARD[i][column] != "  ":
            return i
    return 6


def drop_token(column, player):
    global winner
    token = TOKENS[player]
    row = highest_filled_row(column) - 1
    BOARD[row][column] = token
    if row <= 2 and all((BOARD[row + i][column] == token for i in range(4))):
        winner = player
        return
    for i in range(4):
        c = column - i
        if c < 0 or c > 3:
            continue
        if all((BOARD[row][c + j] == token for j in range(4))):
            winner = player
            return
    for i in range(4):
        sr = row - i
        if sr < 0 or sr > 2:
            continue
        scl = column - i
        scr = column + i
        if 0 <= scl <= 3 and all((BOARD[sr + j][scl + j] == token for j in range(4))):
            winner = player
            return
        if 3 <= scr <= 6 and all((BOARD[sr + j][scr - j] == token for j in range(4))):
            winner = player
            return


player = 1
moves = 0
while True:
    boardState()
    player = 1 - player
    while True:
        column = int(input(f"{PLAYERS[player]} to move: "))
        if not (0 <= column <= 6):
            print("Please enter a number between 0 and 6")
        elif highest_filled_row(column) <= 0:
            print(f"Column {column} is already full")
        else:
            break
    drop_token(column, player)
    moves += 1
    if hasWon() is not None:
        boardState()
        print(f"{PLAYERS[hasWon()]} has won!")
        break
    elif moves >= 6 * 7:
        boardState()
        print("All spaces have been filled!")
        break
