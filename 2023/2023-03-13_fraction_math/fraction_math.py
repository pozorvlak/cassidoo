"""
Write a function that can do the 4 basic operations (add, subtract, multiply
and divide) on two fractions. Return the most simplified form of the result.
You can assume a non-zero denominator in the input, and don’t use any built-in
implementations in your language of choice, if you can!

Example:

> fraction_math("3/4", "add", "3/4")
> "3/2"

> fraction_math("1/8", "multiply", "2/2")
> "1/8"
"""


def fraction_math(lhs, op, rhs):
    lhs = parse(lhs)
    rhs = parse(rhs)
    fn = {"add": add, "multiply": multiply, "subtract": subtract, "divide": divide}[op]
    return to_str(simplify(fn(lhs, rhs)))


def parse(fraction):
    bits = fraction.split("/")
    return (int(bits[0]), int(bits[1]))


def to_str(fraction):
    return f"{fraction[0]}/{fraction[1]}"


def add(lhs, rhs):
    return (lhs[0] * rhs[1] + lhs[1] * rhs[0], lhs[1] * rhs[1])


def multiply(lhs, rhs):
    return (lhs[0] * rhs[0], lhs[1] * rhs[1])


def subtract(lhs, rhs):
    return (lhs[0] * rhs[1] - lhs[1] * rhs[0], lhs[1] * rhs[1])


def divide(lhs, rhs):
    return (lhs[0] * rhs[1], lhs[1] * rhs[0])


def simplify(fraction):
    factor = gcd(fraction[0], fraction[1])
    return (fraction[0] // factor, fraction[1] // factor)


def gcd(a, b):
    if b == 0:
        return a
    if a < b:
        return gcd(b, a)
    return gcd(b, a % b)  # I'm allowed the modulo operator, right?


def test_example1():
    assert fraction_math("3/4", "add", "3/4") == "3/2"


def test_example2():
    assert fraction_math("1/8", "multiply", "2/2") == "1/8"
