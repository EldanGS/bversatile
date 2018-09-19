# https://leetcode.com/problems/validate-binary-search-tree/description/

"""
1st solution.
Complexity analysis:
Time: O(N) - always
Memory: O(N) - always
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        output = []
        self.inOrder(root, output)
        
        for i in range(1, len(output)):
            if output[i-1] >= output[i]:
                return False

        return True

    def inOrder(self, root, output):
        if root is None:
            return
        
        self.inOrder(root.left, output)
        output.append(root.val)
        self.inOrder(root.right, output)

"""
2nd solution, more concise.
Complexity analysis:
Time: O(N) - always
Memory: O(N) - always
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root, minVal = float('inf'), maxVal = float('-inf')):
        if not root:
            return True
        if root.val <= maxVal or root.val >= minVal:
            return False
        return self.isValidBST(root.left, min(root.val, minVal), maxVal) and \
            self.isValidBST(root.right, minVal, max(root.val, maxVal))
