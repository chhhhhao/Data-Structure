from QBase import PriorityQueueBase
import sys, os

sys.path.append("/Users/haochen/Desktop/python/Data Structure/LinkedList")
from PositionalList import PositionalList


class UnsortedPriorityQueue(PriorityQueueBase):
    def __init__(self):
        super().__init__()
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        self._data.add_last(self._Item(key, value))

    def _find_min(self):
        if self.is_empty():
            raise ValueError("Priority queue is empty")
        small = self._data.first()
        walk = self._data.after(small)
        while walk is not None:
            if walk.element() < small.element():
                small = walk
            walk = self._data.after(walk)
        return small

    def min(self):
        p = self._find_min()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        p = self._find_min()
        item = self._data.delete(p)
        return (item._key, item._value)


if __name__ == "__main__":
    P = UnsortedPriorityQueue()
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

