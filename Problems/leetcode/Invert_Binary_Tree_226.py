# https://leetcode.com/problems/invert-binary-tree/description/

"""
Solution.
Complexity analysis:
Time: O(N) - in worst case
Memory: O(N) - in worst case
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        if not root:
            return None
        
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
