"""
Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

Note: If the given node has no in-order successor in the tree, return null.

Example
Example 1:

Input: {1,#,2}, node with value 1
Output: 2
Explanation:
  1
   \
    2
Example 2:

Input: {2,1,3}, node with value 1
Output: 2
Explanation:
    2
   / \
  1   3

"""


def inorderSuccessor(root, p):
    successor = None

    while root:
        if root.val > p.val:
            successor = root
            root = root.left
        else:
            root = root.right

    return successor
