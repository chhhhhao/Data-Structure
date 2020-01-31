from QBase import PriorityQueueBase
import sys, os

sys.path.append("/Users/haochen/Desktop/python/Data Structure/LinkedList")
from PositionalList import PositionalList


class SortedPriorityQueue(PriorityQueueBase):
    def __init__(self):
        super().__init__()
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        newest = self._Item(key, value)
        walk = self._data.last()
        while walk is not None and walk.element() > newest:
            walk = self._data.before(walk)
        if walk is None:
            self._data.add_first(newest)
        else:
            self._data.add_after(walk, newest)

    def min(self):
        if self.is_empty():
            raise ValueError("Priority queue is empty")
        p = self._data.first()
        item = p.element()
        return item._key, item._value

    def remove_min(self):
        if self.is_empty():
            raise ValueError("Priority queue is empty")
        item = self._data.delete(self._data.first())
        return item._key, item._value


if __name__ == "__main__":
    P = SortedPriorityQueue()
    P.add(5, "A")
    P.add(9, "C")
    P.add(3, "B")
    P.add(7, "D")
    print(P.min())
    print(P.remove_min())
    print(P.remove_min())
    print(len(P))
    print(P.remove_min())
    print(P.remove_min())
    print(P.is_empty())
