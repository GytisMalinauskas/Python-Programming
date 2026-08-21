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
    """Throws empty list exceptions"""
    pass


class Node:
    """Initializes new node"""
    def __init__(self, value):
        self.node_value = value
        self.next_node = None

    def value(self):
        """Gets node value"""
        return self.node_value

    def next(self):
        """Gets next node"""
        return self.next_node


class LinkedList:
    """Initializes new linked list"""
    def __init__(self, values=None):
        self.list_head = None
        if values:
            for value in values:
                self.push(value)

    def __iter__(self):
        current = self.list_head
        while current:
            yield current.value()
            current = current.next_node

    def __len__(self):
        current = self.list_head
        value_count = 0
        while current:
            value_count += 1
            current = current.next_node 
        return value_count
    
    def head(self):
        """Gets list head"""
        if self.list_head is None:
            raise EmptyListException("The list is empty.")
        return self.list_head

    def push(self, value):
        """Pushes new value into a new node"""
        node = Node(value)
        node.next_node = self.list_head
        self.list_head = node

    def pop(self):
        """Pops a value from list's head and returns it"""
        if self.list_head is None:
            raise EmptyListException("The list is empty.")
        pop_value = self.list_head.value()
        self.list_head = self.list_head.next_node 
        return pop_value

    def reversed(self):
        """Returns reversed list"""
        current = self.list_head
        new_list = LinkedList()
        while current:
            new_list.push(current.value())
            current = current.next_node
        return new_list