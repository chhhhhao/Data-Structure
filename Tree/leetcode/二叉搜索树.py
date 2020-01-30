from inorder import TreeNode


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.generateSubTrees(1, n) if n else []

    def generateSubTrees(self, start, end):
        if start > end:
            return [None]
        all_trees = []
        for i in range(start, end + 1):
            left_trees = self.generateSubTrees(start, i - 1)
            right_trees = self.generateSubTrees(i + 1, end)

            for l in left_trees:
                for r in right_trees:
                    root = TreeNode(i)  # 创建不同的对象
                    root.left = l
                    root.right = r
                    all_trees.append(root)
        return all_trees


if __name__ == "__main__":
    print(Solution().generateTrees(3))

