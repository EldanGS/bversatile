# https://leetcode.com/problems/binary-tree-level-order-traversal/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: 'TreeNode') -> 'List[List[int]]':
        if not root:
            return []

        level_ordered_tree, queue = [], [root]

        while queue:
            level_ordered_tree.append([node.val for node in queue])
            queue = [node for curr in queue for node in [curr.left, curr.right] if node]

        return level_ordered_tree
