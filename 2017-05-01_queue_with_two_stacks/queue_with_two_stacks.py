"""
This is a classic problem that a bunch of companies have asked:
Write a data structure for a queue using two stacks.

Note: Some companies, instead of having you write the code, have you draw out
the algorithm for this. Solve it however you want!

See https://pozorvlak.livejournal.com/164716.html :-)
"""

class Queue:
    def __init__(self, initial_items=None):
        self.in_stack = []
        self.out_stack = []
        if initial_items is not None:
            self.in_stack.extend(initial_items)

    def add(self, x):
        self.in_stack.append(x)

    def pop(self):
        if len(self.out_stack) == 0:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()

    def __len__(self):
        return len(self.in_stack) + len(self.out_stack)


def test_initial():
    queue = Queue([1, 2, 3, 4, 5])
    out = []
    while len(queue) > 0:
        out.append(queue.pop())
    assert out == [1, 2, 3, 4, 5]


def test_adding():
    queue = Queue()
    for i in range(5):
        queue.add(i)
    out = []
    while len(queue) > 0:
        out.append(queue.pop())
    assert out == [0, 1, 2, 3, 4]
