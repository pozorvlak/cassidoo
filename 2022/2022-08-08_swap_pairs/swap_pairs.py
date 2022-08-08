"""
Given a list, swap every two adjacent nodes. Something to think about: How
would your code change if this were a linked list, versus an array?

Example:

> swap_pairs([1,2,3,4])
> [2,1,4,3]

> swap_pairs([])
> []
"""

from abc import ABC, abstractmethod


class LinkedList(ABC):
    """Linked list abstract base class"""
    value = None
    successor = None

    def __iter__(self):
        node = self
        while not node.is_empty():
            yield node.value
            node = node.successor

    @abstractmethod
    def swap_pairs(self):
        """Swap adjacent elements of the list"""

    @abstractmethod
    def is_empty(self):
        """Is the list empty?"""

    @classmethod
    def from_array(cls, array):
        """Build a linked list from an array"""
        node = Empty()
        for value in reversed(array):
            node = Node(value, node)
        return node


class Empty(LinkedList):
    """End of list marker"""
    def swap_pairs(self):
        return self

    def is_empty(self):
        return True


class Node(LinkedList):
    """A node that contains a value"""
    def __init__(self, value, successor):
        self.value = value
        self.successor = successor

    def swap_pairs(self):
        if self.successor.is_empty():
            return self
        tail = self.successor.successor.swap_pairs()
        return Node(self.successor.value, Node(self.value, tail))

    def is_empty(self):
        return False


def swap_pairs(array):
    """Swap adjacent elements of xs"""
    retval = array.copy()
    for i in range(len(retval) // 2):
        retval[2 * i], retval[2 * i+1] = retval[2 * i + 1], retval[2 * i]
    return retval


def test_example1():
    """Even-length list"""
    assert swap_pairs([1, 2, 3, 4]) == [2, 1, 4, 3]


def test_example2():
    """Empty list"""
    assert swap_pairs([]) == []


def test_example3():
    """Odd-length list"""
    assert swap_pairs([1, 2, 3]) == [2, 1, 3]


def test_example1_list():
    """Even-length list"""
    ans = list(LinkedList.from_array([1, 2, 3, 4]).swap_pairs())
    assert ans == [2, 1, 4, 3]


def test_example2_list():
    """Empty list"""
    assert list(LinkedList.from_array([]).swap_pairs()) == []


def test_example3_list():
    """Odd-length list"""
    ans = list(LinkedList.from_array([1, 2, 3]).swap_pairs())
    assert ans == [2, 1, 3]
