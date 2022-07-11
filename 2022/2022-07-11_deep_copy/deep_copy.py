"""
Given a linked list, such that each node contains an additional random pointer
which could point to any node in the list, or null, make a deep copy of the
list and return the head node of the new copy.

Node definition:

class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
"""


class Node:
    val: int
    next: 'Node'
    random: 'Node'

    def __init__(self, val):
        self.val = val
        self.next = None
        self.random = None

    def __repr__(self):
        return f"Node<{self.val}>"


def make_node(pointer, copies):
    if id(pointer) in copies:
        return copies[id(pointer)]
    else:
        copy = Node(pointer.val)
        copies[id(pointer)] = copy
        return copy


def deep_copy(head):
    copies = {}
    if head is None:
        return None
    pointer = head
    current_copy = make_node(pointer, copies)
    while pointer is not None:
        if pointer.next is not None:
            current_copy.next = make_node(pointer.next, copies)
        if pointer.random is not None:
            current_copy.random = make_node(pointer.random, copies)
        pointer = pointer.next
        current_copy = current_copy.next
    return copies[id(head)]


def test_example():
    nodes = [Node(i) for i in range(10)]
    for i in range(9):
        nodes[i].next = nodes[i+1]
    randoms = [(2, 7), (7, 2), (3, 6), (5, 0), (4, 4)]
    for i, j in randoms:
        nodes[i].random = nodes[j]
    copy = deep_copy(nodes[0])
    copies = [copy]
    while copy.next is not None:
        copies.append(copy.next)
        copy = copy.next
    assert len(copies) == 10
    for i, j in randoms:
        assert copies[i].random == copies[j]
