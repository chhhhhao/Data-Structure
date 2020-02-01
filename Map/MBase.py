from collections.abc import MutableMapping


class MapBase(MutableMapping):
    class _Item:
        __slots__ = "_key", "_value"

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __eq__(self, value):
            return self._key == value._key

        def __ne__(self, value):
            return not (self == value)

        def __lt__(self, value):
            return self._key < value._key
