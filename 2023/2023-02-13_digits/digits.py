"""
Print the digits zero through one hundred without using the characters one to
nine in your code. Get creative!"
"""

from math import pi, sin, cos, asin

zero = sin(pi)
one = int(cos(zero))
two = one + one
five = two * two + one
ten = two * five
hundred = ten * ten

for i in range(hundred + one):
    print(i)
