from QBase import PriorityQueueBase


class HeapPriorityQueue(PriorityQueueBase):
    def __init__(self):
        super().__init__()
        self._data = []

    def _parent(self, j):
        return (j - 1) // 2

    def _left(self, j):
        return 2 * j + 1

    def _right(self, j):
        return 2 * j + 2

    def _has_left(self, j):
        return self._left < len(self._data)

    def _has_right(self, j):
        return self._right < len(self._data)

    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[parent] > self._data[j]:
            self._swap(parent, j)
            self._upheap(parent)

    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            if self._has_right(j):
                right = self._right(j)
                small_child = left if self._data[left] < self._data[right] else right
            else:
                small_child = left
            if self._data[j] > self._data[small_child]:
                self._swap(j, small_child)
                self._downheap(small_child)

    def __len__(self):
        return len(self._data)

    def add(self, k, v):
        self._data.append(self._Item(k, v))
        self._upheap(len(self._data) - 1)

    def min(self):
        if self.is_empty():
            raise ValueError("Priority queue is empty")
        item = self._data[0]
        return item._key, item._value

    def remove_min(self):
        if self.is_empty():
            raise ValueError("Priority queue is empty")
        self._swap(0, len(self._data) - 1)
        item = self._data.pop()
        self._downheap(0)
        return item._key, item._value

