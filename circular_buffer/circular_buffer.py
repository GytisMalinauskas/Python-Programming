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
        self.head = None
        self.tail = 0
        self.list = []
        self.empty = True

    def read(self):
        if self.empty:
            raise BufferEmptyException("Circular buffer is empty")
        index = self.tail
        if self.tail == len(self.list) - 1:
            self.empty = True
        self.tail = (self.tail + 1) % self.capacity
        return self.list[index]

    def write(self, data):
        if len(self.list) == self.capacity:
            raise BufferFullException("Circular buffer is full")
        self.list.append(data)
        self.head = (self.head + 1) % self.capacity
        self.empty = False

    def overwrite(self, data):
        self.list.pop(self.head)
        self.list[self.head].append(data)
        self.head = (self.head + 1) % self.capacity
        
    def clear(self):
        while len(self.list) != 0:
            self.list.pop()
