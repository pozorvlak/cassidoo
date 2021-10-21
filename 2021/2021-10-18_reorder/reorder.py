"""
Given an array of objects A, and an array of indexes B, reorder the objects in
array A with the given indexes in array B.

Example:

let a = [C, D, E, F, G, H];
let b = [3, 0, 4, 1, 2, 5];

$ reorder(a, b) // a is now [D, F, G, C, E, H]
"""

def reorder(xs, indices):
    done = [False for i in indices]
    for i in range(len(indices)):
        j = i
        swap = xs[j]
        while not done[j]:
            ix = indices[j]
            swap, xs[ix] = xs[ix], swap
            done[j] = True
            j = ix
            continue


def test_example():
    a = ["C", "D", "E", "F", "G", "H"]
    b = [3, 0, 4, 1, 2, 5]
    reorder(a, b)
    assert a == ["D", "F", "G", "C", "E", "H"] 

