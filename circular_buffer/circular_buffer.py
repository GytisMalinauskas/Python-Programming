""" A module for managing circular buffer"""

class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """
    def __init__(self, message):
        pass


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """
    def __init__(self, message):
        pass


class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = 0
        self.tail = 0
        self.list = []
        self.empty = True

    def read(self):
        """Reads value that is in the tail if circular buffer is not empty"""
        if self.empty:
            raise BufferEmptyException("Circular buffer is empty")
        return_value = self.list[self.tail]
        self.list.pop(self.tail)
        if len(self.list) == 0:
            self.empty = True
        if len(self.list) != 0:
            self.tail = self.tail % len(self.list)
        return return_value

    def write(self, data):
        """Writes value to the end of the list if circular buffer is not full"""
        if len(self.list) == self.capacity:
            raise BufferFullException("Circular buffer is full")
        self.list.append(data)
        self.head = (self.head + 1) % self.capacity
        if self.empty:
            self.empty = False

    def overwrite(self, data):
        """Overwrites value at tail index"""
        if len(self.list) == self.capacity:
            self.list[self.tail] = data
            self.tail = (self.tail + 1) % self.capacity
            self.empty = False
        if len(self.list) < self.capacity:
            self.write(data)
        
    def clear(self):
        """Clears the circular buffer by poping each value"""
        while len(self.list) != 0:
            self.list.pop()
        self.head = 0
        self.tail = 0
        self.empty = True
