"""
You have a faulty keyboard. Whenever you type a vowel on it (a,e,i,o,u,y),
it reverses the string that you have written, instead of typing the
character. Typing other characters works as expected. Given a string, return
what will be on the screen after typing with your faulty keyboard.

Example:

> faulty_keyboard('string')
> 'rtsng'

> faulty_keyboard('hello world!')
> 'w hllrld!'
"""

def faulty_keyboard(string):
    output = []
    for c in string:
        if c in "AEIOUaeiou":
            output = output[::-1]
        else:
            output.append(c)
    return "".join(output)


def test_example1():
    assert faulty_keyboard('string') == 'rtsng'


def test_example2():
    assert faulty_keyboard('hello world!') == 'w hllrld!'
