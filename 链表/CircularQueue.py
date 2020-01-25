class Empty(Exception):
    pass


class LinkedQueue:
    class _Node:
        __slots__ = "_element", "_next"

        def __init__(self, element, next_node):
            self._element = element
            self._next = next_node

    def __init__(self):
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._tail._next._element

    def dequeue(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        old_head = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = old_head._next
        self._size -= 1

        return old_head._element

    def enqueue(self, e):
        newNode = self._Node(e, None)
        if self.is_empty():
            newNode._next = newNode
        else:
            newNode._next = self._tail._next
            self._tail._next = newNode
        self._tail = newNode
        self._size += 1

    def rotate(self):
        if self._size > 0:
            self._tail = self._tail._next
