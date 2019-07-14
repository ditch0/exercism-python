from collections import deque


class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer(deque):
    def __init__(self, capacity):
        super().__init__()
        self._capacity = capacity

    def read(self):
        if self.is_empty:
            raise BufferEmptyException('Buffer is empty')
        return self.pop()

    def write(self, data):
        if self.is_full:
            raise BufferFullException('Buffer is full')
        self.appendleft(data)

    def overwrite(self, data):
        if self.is_full:
            self.read()
        self.write(data)

    @property
    def is_full(self):
        return len(self) == self._capacity

    @property
    def is_empty(self):
        return len(self) == 0
