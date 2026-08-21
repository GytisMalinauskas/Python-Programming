"""This is a module of linked list"""

""" 
    Singly linked list contains data and the reference to next node,
    and null value at the end and all you need to know is the location of the head.
    Doubly linked list is the same but you also have previous node
    reference and then you can traverse back.
    Circular linked list does not end with null, its last value is
    considered a tails and node after is the beggining of the list.
"""

class EmptyListException(Exception):
    pass


class Node:
    def __init__(self, value):
        self.node_value = value
        self.next_node = None

    def value(self):
        return self.node_value

    def next(self):
        return self.next_node


class LinkedList:
    def __init__(self, values=None):
        self.list_head = None

    def __iter__(self):
        pass

    def __len__(self):
        pass

    def head(self):
        return self.list_head

    def push(self, value):
        node = Node(value)
        node.next_node = self.list_head
        self.list_head = node

    def pop(self):
        pass

    def reversed(self):
        pass
