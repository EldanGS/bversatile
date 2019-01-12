# https://leetcode.com/problems/average-of-levels-in-binary-tree/description/

"""
Solution.
Used: BFS algortihm
Complexity analysis:
Time: O(N + M) - in worst case
Memory: O(N) - in worst case
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        q = []
        q.append(root)
        result = []

        while q:
            n = len(q)
            total = 0
            
            for i in range(n):
                v = q[0]
                del q[0]
                total += v.val
                
                if v.left:
                    q.append(v.left)
                if v.right:
                    q.append(v.right)
            
            result.append(total / n)
        
        return result
            
            
