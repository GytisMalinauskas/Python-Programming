"""This is a module of linked list"""

""" 
    Singly linked list contains data and the reference to next node,
    and null value at the end and all you need to know is the location of the head.
    Doubly linked list is the same but you also have previous node
    reference and then you can traverse back.
    Circular linked list does not end with null, its last value is
    considered a tails and node after is
"""

class EmptyListException(Exception):
    pass


class Node:
    def __init__(self, value):
        pass

    def value(self):
        pass

    def next(self):
        pass


class LinkedList:
    def __init__(self, values=None):
        pass

    def __iter__(self):
        pass

    def __len__(self):
        pass

    def head(self):
        pass

    def push(self, value):
        pass

    def pop(self):
        pass

    def reversed(self):
        pass
