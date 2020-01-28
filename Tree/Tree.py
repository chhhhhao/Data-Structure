import sys

sys.path.append("/Users/haochen/Desktop/python/Data Structure")

from LinkedList import LinkedQueue


class Tree:
    class Position:
        def element(self):
            raise NotImplementedError("must be implemented by subclass")

        def __eq__(self, value):
            raise NotImplementedError("must be implemented by subclass")

        def __ne__(self, value):
            return not (self == value)

    def root(self):
        raise NotImplementedError("must be implemented by subclass")

    def parent(self, p):
        raise NotImplementedError("must be implemented by subclass")

    def num_children(self, p):
        raise NotImplementedError("must be implemented by subclass")

    def children(self, p):
        raise NotImplementedError("must be implemented by subclass")

    def __len__(self):
        raise NotImplementedError("must be implemented by subclass")

    def is_root(self, p):
        return self.root() == p

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def is_empty(self):
        return len(self) == 0

    def depth(self, p):
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _height2(self):
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(p) for p in self.children(p))

    def height(self, p=None):
        if p is None:
            p = self.root()
        return self._height2(p)

    def positions(self):
        return self.preorder()

    def __iter__(self):
        for p in self.positions():
            yield p.element()

    # 先序遍历
    def preorder(self):
        # Generator
        if not self.is_empty():
            return self._subtree_preorder(self.root())
        return None

    def _subtree_preorder(self, p):
        # Generator
        yield p
        for c in self.children(p):
            for other in self._subtree_preorder(c):
                yield other

    def postorder(self):
        if not self.is_empty():
            return self._subtree_postorder(self.root())
        return None

    def _subtree_postorder(self, p):
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other
        yield p

    def breadthfirst(self):
        if not self.is_empty():
            fringe = LinkedQueue()
            fringe.enqueue(self.root())
            while not fringe.is_empty():
                p = fringe.dequeue()
                yield p
                for c in self.children(p):
                    fringe.enqueue(c)
