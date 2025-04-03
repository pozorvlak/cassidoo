"""
Implement the Luhn algorithm to validate a credit card number. Bonus points if you can identify what brand of credit card the user inputted!

Example:

> luhn_check(123456789)
> false

> luhn_check(5555555555554444)
> true // Mastercard
"""

def luhn_check(x):
    digits = [int(c) for c in str(x)][::-1]
    check_digit = digits.pop(0)
    s = 0
    for i, d in enumerate(digits):
        term = 2 * d if i % 2 == 0 else d
        s += (term % 10) + (term // 10)
    print(f"Check digit is {check_digit}, should be 10 - ({s} % 10)")
    return check_digit == 10 - (s % 10)


def test_example1():
    assert not luhn_check(123456789)


def test_example2():
    assert luhn_check(5555555555554444) #  Mastercard


def test_example_wikipedia():
    assert luhn_check(79927398713)
