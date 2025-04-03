"""
Given a string s, you are allowed to delete at most k characters. Find if the
string can be a palindrome after deleting at most k characters.

Example:

> k_pal('abcweca', 2)
> true

> k_pal('acxcb', 1)
> false
"""

def k_pal(s, k):



def test_example1():
    assert k_pal('abcweca', 2) == True

def test_example2():
    assert k_pal('acxcb', 1) == False
