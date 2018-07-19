# https://leetcode.com/problems/binary-tree-paths/description/


"""
Solution.
Used: DFS algortihm
Complexity analysis:
Time: O(N * M)
Memory: O(N * M) in worst case
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        path = []
        if not root:
            return path
        
        def dfs(root, value):
            if not root.left and not root.right:
                path.append(value)
            if root.left:
                dfs(root.left, value + '->' + str(root.left.val))
            if root.right:
                dfs(root.right, value + '->' + str(root.right.val))
        
        dfs(root, str(root.val))
        
        return path
        
