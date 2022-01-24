"""
You are given three files named first_page.txt, second_page.txt, and
third_page.txt with the occurrence of at least one palindrome in each of them.
Write a script to find the following:

    The exact number of palindromes in each file.
    The line numbers of the palindromes in each file.
"""

import re


WORD = re.compile(r'[A-Za-z]+')


def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]


def words(line):
    return WORD.findall(line)


def process_file(fh):
    count, line_numbers = 0, set()
    for i, line in enumerate(fh):
        for word in words(line):
            if is_palindrome(word):
                count += 1
                line_numbers.add(i)
    return count, line_numbers


def main():
    for filename in ["first_page.txt", "second_page.txt", "third_page.txt"]:
        with open(filename) as fh:
            count, line_numbers = process_file(fh)
        print(f"{filename}: {count} palindromes, on lines {line_numbers}")


if __name__ == '__main__':
    main()


def test_process_file():
    lines = [
        "This is a test.",
        "Do not be alarmed, foof.",
        "No palindromes on this line, nosiree",
        "Satanoscillatemymetallicsonatas boob wow",
        "mawaM",
    ]
    count, line_numbers = process_file(lines)
    assert count == 6
    assert line_numbers == {0, 1, 3, 4}


def test_words():
    line = "Do not be alarmed, foof."
    assert words(line) == ["Do", "not", "be", "alarmed", "foof"]
