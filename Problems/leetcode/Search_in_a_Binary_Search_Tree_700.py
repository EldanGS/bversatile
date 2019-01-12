# https://leetcode.com/problems/search-in-a-binary-search-tree/description/

"""
Solution.
Complexity analysis:
Time: O(logN) - in worst case
Memory: O(logN) - in worst case
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNodes
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.val < val:
            return self.searchBST(root.right, val)
        elif root.val > val:
            return self.searchBST(root.left, val)
        else:
            return root