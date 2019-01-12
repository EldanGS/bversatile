# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

"""
Solution.
Used: DFS algortihm
Complexity analysis:
Time: O(N)
Memory: O(N) in worst case, stack memory
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1