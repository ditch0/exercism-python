from collections import deque


class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer(object):
    def __init__(self, capacity):
        self._capacity = capacity
        self._storage = deque()

    def read(self):
        if len(self._storage) > 0:
            return self._storage.pop()
        raise BufferEmptyException('Buffer is empty')

    def write(self, data):
        if not self.is_full:
            self._storage.appendleft(data)
        else:
            raise BufferFullException('Buffer is full')

    def overwrite(self, data):
        if self.is_full:
            self.read()
        self.write(data)

    def clear(self):
        self._storage.clear()

    @property
    def is_full(self):
        return len(self._storage) == self._capacity
