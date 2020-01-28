class Empty(Exception):
    pass


class ArrayQueue:

    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * self.DEFAULT_CAPACITY
        self._front = 0
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def _resize(self, cap):
        old = self._data
        old_front = self._front
        self._data = [None] * cap
        for k in range(self._size):
            self._data[k] = old[(old_front + k) / len(old)]
        self._front = 0

    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(len(self._data * 2))
        rear = (self._front + self._size) % len(self._data)
        self._data[rear] = e
        self._size += 1
