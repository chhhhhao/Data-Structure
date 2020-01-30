# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from inorder import TreeNode

# 广度优先的另一种实现
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        def BFS(d, q, levels):
            if len(q) == 0:
                return
            tmp = []
            S = []
            while len(q) > 0:
                l = q.pop(0)
                if d == len(levels):
                    levels.append([])
                if d % 2 == 1:
                    S.append(l.val)
                else:
                    levels[d].append(l.val)
                if l.left:
                    tmp.append(l.left)
                if l.right:
                    tmp.append(l.right)
            if d % 2 == 1:
                while len(S) > 0:
                    levels[d].append(S.pop())
            BFS(d + 1, tmp, levels)

        levels = []
        if not root:
            return []
        else:
            BFS(0, [root], levels)
        return levels

