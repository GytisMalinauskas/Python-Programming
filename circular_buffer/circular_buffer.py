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
        self.tail = None
        self.list = []

    def read(self):
        index = self.tail
        self.tail = (self.tail + 1) % self.capacity
        return self.list[index]

    def write(self, data):
        pass

    def overwrite(self, data):
        pass

    def clear(self):
        pass
