"""This is a module of linked list"""

""" 
    Linked list contains data and the reference to next node,
    and null value at the end(singly linked list).
    All you need to know is the location of the head.
    If you have previous node reference, then you can also
    traverse back (doubly linked list).
    Circular linked list does not end with nul
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
