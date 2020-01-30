# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        if (root.left is None or root.left.val < root.val) and (
            root.right is None or root.right.val > root.val
        ):
            left = root.left
            right = root.right
        else:
            return False

        if not (self.isValidBST(left) and self.isValidBST(right)):
            return False

        while left is not None:
            max = left.val
            if max >= root.val:
                return False
            left = left.right
        while right is not None:
            min = right.val
            if min <= root.val:
                return False
            right = right.left
        return True
