"""
Inorder Predecessor in BST
Given a binary search tree and a node in it, find the in-order predecessor of that node in the BST.

Example

Example1
Input: root = {2,1,3}, p = 1
Output: null

Example2
Input: root = {2,1}, p = 2
Output: 1
Notice
If the given node has no in-order predecessor in the tree, return null

"""


# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    def inorder_predecessor(self, root, p):

        self.predecessor, self.last_node = None, None

        def inorder_traversal(node, p):
            if not node or self.predecessor:
                return

            inorder_traversal(node.left, p)

            if node == p:
                self.predecessor = self.last_node
            else:
                self.last_node = node

            inorder_traversal(node.right, p)

        inorder_traversal(root, p)

        return self.predecessor.val


if __name__ == '__main__':
    p1 = TreeNode(2)
    p2 = TreeNode(1)
    p3 = TreeNode(3)
    p4 = TreeNode(0)

    p1.left = p2
    p1.right = p3
    p2.left = p4

    solution = Solution()

    print(solution.inorder_predecessor(p1, p1))
