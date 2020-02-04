import sys, os

sys.path.append("/Users/haochen/Desktop/python/Data Structure")
from Tree.LinkedBTree import LinkedBinaryTree
from Map.MBase import MapBase


class TreeMap(LinkedBinaryTree, MapBase):
    class Position(LinkedBinaryTree.Position):
        def __init__(self, container, node):
            super().__init__(container, node)

        def key(self):
            return self.element()._key

        def value(self):
            return self.element()._value

    def _subtree_search(self, p, k):
        if k == p.key():
            return p
        elif k < p.key():
            if self.left(p) is not None:
                return self._subtree_search(self.left(p), k)
        else:
            if self.right(p) is not None:
                return self._subtree_search(self.right(p), k)
        return p

    def _subtree_first_position(self, p):
        walk = p
        while self.left(walk) is not None:
            walk = self.left(walk)
        return walk

    def _subtree_last_position(self, p):
        walk = p
        while self.right(p) is not None:
            walk = self.right(walk)
        return walk

    def first(self):
        return self._subtree_first_position(self.root()) if len(self) > 0 else None

    def last(self):
        return self._subtree_last_position(self.root()) if len(self) > 0 else None

    def before(self, p):
        self._validate(p)
        if self.left(p):
            return self._subtree_last_position(self.left(p))
        else:
            walk = p
            ancestor = self.parent(p)
            while ancestor is not None and walk == self.left(ancestor):
                walk = ancestor
                ancestor = self.parent(p)
            return ancestor

    def after(self, p):
        self._validate(p)
        if self.right(p):
            return self._subtree_first_position(self.right(p))
        else:
            walk = p
            ancestor = self.parent(p)
            while ancestor is not None and walk == self.right(ancestor):
                walk = ancestor
                ancestor = self.parent(walk)
            return ancestor

    def find_position(self, k):
        if self.is_empty():
            return None
        else:
            p = self._subtree_search(self.root(), k)
            self._rebalance_access(p)
            return p

    def find_min(self):
        if self.is_empty():
            return None
        else:
            p = self.first()
            return (p.key(), p.value())

    def find_ge(self, k):
        if self.is_empty():
            return None
        else:
            p = self.find_position(k)
            if p.key() < k:
                p = self.after(p)
            return (p.key(), p.value()) if p is not None else None

    def find_range(self, start, stop):
        if not self.is_empty():
            if start is None:
                start = self.first()
            else:
                p = self.find_position(k)
                if p.key() < k:
                    p = self.after(p)
                while p is not None and (stop is None or p.key() < stop):
                    yield p
                    p = self.after(p)

    def __getitem__(self, k):
        if self.is_empty():
            raise KeyError("Key Error: " + repr(k))
        else:
            p = self._subtree_search(self.root(), k)
            self._rebalance_access(p)
            if p.key() == k:
                return p.value()
            else:
                raise KeyError("Key Error: " + repr(k))

    def __setitem__(self, k, v):
        if self.is_empty():
            self._add_root(self._Item(k, v))
        else:
            p = self._subtree_search(self.root(), k)
            if p.key() == k:
                p.element()._value = v
                self._rebalance_access(p)
            else:
                item = self._Item(k, v)
                if p.key() > k:
                    leaf = self._add_left(p, item)

                else:
                    leaf = self._add_right(p, item)
                self._rebalance_insert(leaf)

    def __iter__(self):
        p = self.first()
        while p is not None:
            yield p.key()
            p = self.after(p)

    def delete(self, p):
        self._validate(p)
        if self.left(p) and self.right(p):
            r = self.before(p)
            self._replace(p, r.element())
            p = r
        parent = self.parent(p)
        self._delete(p)
        self._rebalance_delete(parent)

    def __delitem__(self, k):
        if not self.is_empty():
            p = self._subtree_search(self.root(), k)
            if p.key() == k:
                self.delete(p)
                return
            self._rebalance_access(p)
        raise KeyError("Key Error: " + repr(k))

    def _rebalance_access(self, p):
        pass

    def _rebalance_delete(self, p):
        pass

    def _rebalance_insert(self, p):
        pass

    def _relink(self, parent, child, make_left_child):
        # allow child to be None
        if make_left_child:
            parent._left = child
        else:
            parent._right = child
        if child is not None:
            child._parent = parent

    def _rotate(self, p):
        # rotate p above its parent
        x = p._node
        y = x._parent
        z = y._parent
        if z is None:
            self._root = x
            x._parent = None
        else:
            self._relink(z, x, y == z._left)
        if x == y._left:
            self._relink(y, x._right, True)
            self._relink(x, y, False)
        else:
            self._relink(y, x._left, False)
            self._relink(x, y, True)

    def _reconstructure(self, x):

        y = self.parent(x)
        z = self.parent(y)
        if (y == self.left(z)) == (x == self.left(y)):
            self._rotate(y)
            return y
        else:
            self._rotate(x)
            self._rotate(x)
            return x

