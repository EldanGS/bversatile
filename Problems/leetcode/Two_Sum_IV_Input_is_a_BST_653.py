# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/


"""
1st solution, naive method with memory
Complexity analysis:
Time: O(N) - in worst case
Memory: O(N) - in worst case
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    data = dict()
    def __init__(self):
        self.data = dict()
        
    def findTarget(self, root, k):
        if not root:
            return False
        
        if self.data.get(root.val):
            return True
        self.data[root.val] = self.data[k - root.val] = True
        
        return self.findTarget(root.left, k) or self.findTarget(root.right, k)
        
        
        
        