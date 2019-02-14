# https://leetcode.com/problems/minimum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        q = collections.deque([(root, 1)])
        while q:
            node, distance = q.popleft()
            if not node.left and not node.right:
                return distance

            if node.left:
                q.append((node.left, distance + 1))
            if node.right:
                q.append((node.right, distance + 1))

        return -1
