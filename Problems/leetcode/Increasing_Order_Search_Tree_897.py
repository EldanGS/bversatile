# https://leetcode.com/contest/weekly-contest-100/problems/increasing-order-search-tree/

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
    data = []
    def __init__(self):
        self.data = []
    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        self.data.append(root)
        self.inorder(root.right)
        
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.inorder(root)
        
        n = len(self.data)
        for i in range(1, n):
            self.data[i - 1].left = None
            self.data[i - 1].right = self.data[i]
        self.data[n - 1].left = self.data[n - 1].right = None
        
        return self.data[0]