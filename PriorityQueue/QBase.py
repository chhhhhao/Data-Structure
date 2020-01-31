class PriorityQueueBase:
    class _Item(object):
        __slots__ = "_key", "_value"

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, value):
            return self._key < value._key

    def is_empty(self):
        return len(self) == 0

