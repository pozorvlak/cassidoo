"""
Write 2 functions that sort a stack (one function with the smallest items on
top, the other with the largest items on top).

Try to do this one using only stacks, no other things like arrays, lists, or
queues. You have access to the functions pop, peek, push, and isEmpty.
"""

from hypothesis import given, strategies as st


class Stack():
    def __init__(self, initial_items=None):
        self.contents = []
        if initial_items is not None:
            self.contents.extend(initial_items)

    def pop(self):
        return self.contents.pop()

    def peek(self):
        return self.contents[-1]

    def push(self, value):
        self.contents.append(value)

    def is_empty(self):
        return len(self.contents) == 0


def copy_stack(source, target):
    while not source.is_empty():
        target.push(source.pop())


def sort_stack(stack, asc):
    if stack.is_empty():
        return
    pivot = stack.pop()
    lt = Stack()
    ge = Stack()
    while not stack.is_empty():
        x = stack.pop()
        if x < pivot:
            lt.push(x)
        else:
            ge.push(x)
    sort_stack(lt, not asc)
    sort_stack(ge, not asc)
    first, second = (lt, ge) if asc else (ge, lt)
    copy_stack(first, stack)
    stack.push(pivot)
    copy_stack(second, stack)


def sort_asc(stack):
    return sort_stack(stack, True)


def sort_desc(stack):
    return sort_stack(stack, False)


@given(st.lists(st.integers()))
def test_sort_asc(xs):
    stack = Stack(xs)
    sort_asc(stack)
    assert stack.contents == sorted(xs)


@given(st.lists(st.integers()))
def test_sort_desc(xs):
    stack = Stack(xs)
    sort_desc(stack)
    assert stack.contents == sorted(xs, reverse=True)
