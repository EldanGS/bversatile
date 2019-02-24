# https://leetcode.com/problems/binary-tree-maximum-path-sum/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.max_sum = None

    def maxPathSum(self, root: TreeNode) -> int:
        def max_path(node):
            if not node:
                return 0
            left = max_path(node.left)
            right = max_path(node.right)

            self.max_sum = max(self.max_sum, left + node.val + right)
            return max(0, max(left, right) + node.val)

        self.max_sum = float('-inf')
        max_path(root)

        return self.max_sum
