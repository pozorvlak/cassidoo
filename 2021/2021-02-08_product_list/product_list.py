#!/usr/bin/env python

"""
Implement a ProductList class that has two methods, add(n) (which pushes the value n to the back of the list) and product(m) (which returns the product of the last m numbers in the list). David made an awesome template for submitting your solutions, if you’d like to use it!

Usage:

ProductList p = new ProductList();
p.add(7);         // [7]
p.add(0);         // [7,0]
p.add(2);         // [7,0,2]
p.add(5);         // [7,0,2,5]
p.add(4);         // [7,0,2,5,4]
p.product(3);     // return 40 because 2 * 5 * 4
"""

class ProductList:
    def __init__(self):
        self.contents = []

    def add(self, n):
        self.contents.append(n)

    def product(self, m):
        ret = 1
        for n in self.contents[-m:]:
            ret *= n
        return ret


def test_example():
    p = ProductList()
    p.add(7)
    p.add(0)
    p.add(2)
    p.add(5)
    p.add(4)
    assert p.product(3) == 40


def test_two_lists_do_not_interfere():
    p1 = ProductList()
    p2 = ProductList()
    p1.add(7)
    p1.add(9)
    p2.add(4)
    p2.add(3)
    assert p1.product(2) == 63
    assert p2.product(2) == 12
