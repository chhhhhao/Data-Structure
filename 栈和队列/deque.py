class Empty(Exception):
    pass


class Deque:

    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * self.DEFAULT_CAPACITY
        self._front = 0
        self._size = 0

    def __len__(self):
        return self._size

    # 用于测试，不属于双端队列的操作
    def __repr__(self):
        return self._data.__repr__()

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._data[self._front]

    def last(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._data[(self._front + self._size - 1) % len(self._data)]

    def delete_first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def delete_last(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        answer = self._data[(self._front + self._size - 1) % len(self._data)]
        self._data[(self._front + self._size - 1) % len(self._data)] = None
        self._size -= 1

    def _resize(self, cap):
        old = self._data
        old_front = self._front
        self._data = [None] * cap
        for k in range(self._size):
            self._data[k] = old[(old_front + k) % len(old)]
        self._front = 0

    def add_last(self, e):
        if self._size == len(self._data):
            self._resize(len(self._data * 2))
        rear = (self._front + self._size) % len(self._data)
        self._data[rear] = e
        self._size += 1

    def add_first(self, e):
        if self._size == len(self._data):
            self._resize(len(self._data * 2))
        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = e
        self._size += 1


if __name__ == "__main__":
    D = Deque()
    D.add_last(5)
    D.add_first(3)
    D.add_first(7)
    print(D)
    D.delete_last()
    print(D)
    print(len(D))
    D.delete_last()
    print(D)
    print("D is empty:", D.is_empty())
    print(D.last())
