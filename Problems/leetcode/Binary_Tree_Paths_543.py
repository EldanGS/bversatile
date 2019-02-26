# https://leetcode.com/problems/diameter-of-binary-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []

        path = []

        def traverse(node, value):
            if not node.left and not node.right:
                path.append(value)

            if node.left:
                traverse(node.left, value + '->' + str(node.left.val))

            if node.right:
                traverse(node.right, value + '->' + str(node.right.val))

        traverse(root, str(root.val))

        return path
