# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        answer = []
        self._subtree_inorder(root, answer)
        return answer

    def _subtree_inorder(self, p, answer):
        if p.left is not None:
            self._subtree_inorder(p.left, answer)
        answer.append(p.val)
        if p.right is not None:
            self._subtree_inorder(p.right, answer)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = None
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(Solution().inorderTraversal(root))
