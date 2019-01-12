# https://leetcode.com/problems/binary-tree-pruning/description/

"""
Solution.
Used: DFS algortihm
Complexity analysis:
Time: O(N) - in worst case
Memory: O(N) - ?
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        
        if not root.left and not root.right and not root.val:
            return None
        return root
