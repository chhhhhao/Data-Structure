import sys, os

sys.path.append("/Users/haochen/Desktop/python/Data Structure")

from TreeMap.TMap import TreeMap


class AVLTreeMap(TreeMap):
    class _Node(TreeMap._Node):
        def __init__(self, element=None, parent=None, left=None, right=None):
            super().__init__(element=element, parent=parent, left=left, right=right)
            self._height = 0

        def left_height(self):
            return self._left._height if self._left is not None else 0

        def right_height(self):
            return self._right._height if self._right is not None else 0

    def _recompute_height(self, p):
        node = self._validate(p)
        node._height = 1 + max(node.left_height() + node.right_height())

    def _isBalanced(self, p):
        node = self._validate(p)
        return abs(node.left_height() - node.right_height()) <= 1

    def _tall_child(self, p, favorleft=False):
        node = self._validate(p)
        if node.left_height() + (1 if favorleft else 0) > node.right_height():
            return self.left(p)
        else:
            return self.right(p)
    def _grand_child(self,p):
        tall_child = self._tall_child(p)
        favor = (tall_child == self.left(p)
        return self._tall_child(tall_child,favor)

    def _rebalance(self,p):
        while p is not None:
            node = self._validate(p)
            old_height = node._height
            if not self._isBalanced(p):
                p = self._reconstructure(self._grand_child(p))
                self._recompute_height(self.left(p))
                self._recompute_height(self.right(p))
            self._recompute_height(p)
            if p._node._height == old_height:
                p = None
            else:
                p = self.parent(p)
    def _rebalance_insert(self, p):
        self._rebalance(p)
        
    def _rebalance_delete(self, p):
        self._rebalance(p)
            
