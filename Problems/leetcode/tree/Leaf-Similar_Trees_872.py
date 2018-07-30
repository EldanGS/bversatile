# https://leetcode.com/problems/leaf-similar-trees/description/

"""
Solution.
Used: DFS algortihm
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
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.findLeaf(root1) == self.findLeaf(root2)
    
    def findLeaf(self, root):
        if not root: return []
        if not (root.left or root.right): return [root.val]
        return self.findLeaf(root.left) + self.findLeaf(root.right)
