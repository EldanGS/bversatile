# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/description/

"""
Solution.
Used: DFS algortihm
Complexity analysis:
Time: O(N * M) - in worst case
Memory: O(M) - in worst case
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children # list
"""
class Solution(object):
    max_depth = 0
    def __init__(self):
        self.max_depth = 0
        
    def dfs(self, root, level):
        if not root:
            return;
        self.max_depth = max(self.max_depth, level)
        for node in root.children:
            self.dfs(node, level + 1)
        
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        self.dfs(root, 1)
        
        return self.max_depth

