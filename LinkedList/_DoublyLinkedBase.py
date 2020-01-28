class Empty(Exception):
    pass


class _DoublyLinkedBase:
    class _Node:
        __slots__ = "_element", "_next", "_prev"

        def __init__(self, element, prev_node, next_node):
            self._element = element
            self._prev = prev_node
            self._next = next_node

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        newNode = self._Node(e, predecessor, successor)
        predecessor._next = newNode
        successor._prev = newNode
        self._size += 1
        return newNode

    def _delete_node(self, node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element

