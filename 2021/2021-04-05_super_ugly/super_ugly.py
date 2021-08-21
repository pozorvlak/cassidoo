"""
Given an integer n and a sorted array of prime integers called primes, return
the nth “super ugly number”. A “super ugly number” is a positive number whose
all prime factors are in the array primes.

Example:

$ superUgly(1, [2,3,5])
$ 1
$ superUgly(11, [2,7,13,19])
$ 28
"""

from heapq import heappush, heappop

from more_itertools import take, nth


def super_uglies(primes):
    heap = []
    heappush(heap, 1)
    last = 0
    while len(heap) > 0:
        i = heappop(heap)
        if i != last:
            yield i
            last = i
        for p in primes:
            heappush(heap, p * i)
    

def super_ugly(n, primes):
    return nth(super_uglies(primes), n - 1) 


def test_example1():
    assert super_ugly(1, [2, 3, 5]) == 1


def test_example2():
    assert super_ugly(11, [2, 7, 13, 19]) == 28


def test_super_uglies():
    assert take(11, super_uglies([2, 3, 5])) == \
            [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15]
