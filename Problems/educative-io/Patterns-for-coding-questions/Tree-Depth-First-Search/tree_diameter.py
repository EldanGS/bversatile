"""
https://www.educative.io/courses/grokking-the-coding-interview/xVV1jA29YK9

Given a binary tree, find the length of its diameter. The diameter of a tree
is the number of nodes on the longest path between any two leaf nodes. The
diameter of a tree may or may not pass through the root.

Note: You can always assume that there are at least two leaf nodes in the given tree.
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeDiameter:

    def __init__(self):
        self.tree_diameter = 0

    def find_diameter_helper(self, node):
        if not node:
            return 0

        left_subtree = self.find_diameter_helper(node.left)
        right_subtree = self.find_diameter_helper(node.right)
        self.tree_diameter = max(self.tree_diameter,
                                 left_subtree + right_subtree + 1)

        return max(left_subtree, right_subtree) + 1

    def find_diameter(self, root):
        self.find_diameter_helper(root)
        return self.tree_diameter


def main():
    tree_diameter = TreeDiameter()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    print("Tree Diameter: " + str(tree_diameter.find_diameter(root)))
    root.left.left = None
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    root.right.left.right.left = TreeNode(10)
    root.right.right.left.left = TreeNode(11)
    print("Tree Diameter: " + str(tree_diameter.find_diameter(root)))


main()
