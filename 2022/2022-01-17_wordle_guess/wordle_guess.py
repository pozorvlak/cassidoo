"""
Using the rules of Wordle, given a guessWord and a solution_word, return a set of emojis returned from the guessWord.

Example:

let solution_word = "fudge"

$ wordle_guess("reads", solution_word)
$ "⬛🟨⬛🟨⬛"

$ wordle_guess("lodge", solution_word)
$ "⬛⬛🟩🟩🟩"
"""

def wordle_guess(guess, solution):
    letters = set(solution)
    output = ""
    for i, c in enumerate(guess):
        if solution[i] == c:
            output += "🟩"
        elif c in letters:
            output += "🟨"
        else:
            output += "⬛"
    return output


def test_examples():
    solution_word = "fudge"
    assert wordle_guess("reads", solution_word) == "⬛🟨⬛🟨⬛"
    assert wordle_guess("lodge", solution_word) == "⬛⬛🟩🟩🟩"
