# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.lca = None

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        def lca_helper(node):
            if not node:
                return False

            left = lca_helper(node.left)
            right = lca_helper(node.right)

            mid = node == p or node == q
            if mid + left + right >= 2:
                self.lca = node

            return mid or left or right

        lca_helper(root)

        return self.lca
