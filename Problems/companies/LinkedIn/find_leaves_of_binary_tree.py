"""
Given a binary tree, collect a tree's nodes as if you were doing this:
Collect and remove all leaves, repeat until the tree is empty.



Example:

Input: [1,2,3,4,5]

          1
         / \
        2   3
       / \
      4   5

Output: [[4,5,3],[2],[1]]


Explanation:

1. Removing the leaves [4,5,3] would result in this tree:

          1
         /
        2


2. Now removing the leaf [2] would result in this tree:

          1


3. Now removing the leaf [1] would result in the empty tree:

          []

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def dfs(self, node, result):
        if not node:
            return -1

        level = max(self.dfs(node.left, result),
                    self.dfs(node.right, result)) + 1
        if level >= len(result):
            result.append([])

        result[level].append(node.val)
        return level

    def findLeaves(self, root: TreeNode) -> list:
        if not root:
            return []

        result = []
        self.dfs(root, result)
        return result
