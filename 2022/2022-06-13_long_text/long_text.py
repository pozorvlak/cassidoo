"""
Create a loooong teeeext generator that takes in a string and an integer n, and
multiplies the vowels in the string by n.
"""


def long_text(text, n):
    """Multiply the vowels in text by n"""
    for vowel in "aeiou":
        text = text.replace(vowel, vowel * n)
        text = text.replace(vowel.upper(), vowel.upper() * n)
    return text


def test_example1():
    assert long_text('hello world', 3) == 'heeellooo wooorld'


def test_example2():
    assert long_text('lol', 10) == 'looooooooool'
