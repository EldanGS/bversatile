"""
https://www.educative.io/courses/grokking-the-coding-interview/B89q6NpX0Vx
Find the path with the maximum sum in a given binary tree. Write a
function that returns the maximum sum. A path can be defined as a sequence of
nodes between any two nodes and doesn’t necessarily pass through the root.

"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_sum_helper(node):
    if not node:
        return 0
    global max_sum
    left_subtree_sum = max_sum_helper(node.left)
    right_subtree_sum = max_sum_helper(node.right)
    path_sum = left_subtree_sum + right_subtree_sum + node.val
    max_sum = max(max_sum, path_sum)

    return max(left_subtree_sum, right_subtree_sum) + node.val


def find_maximum_path_sum(root):
    if not root:
        return 0

    global max_sum
    max_sum = float('-inf')
    max_sum_helper(root)
    return max_sum


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    print("Maximum Path Sum: " + str(find_maximum_path_sum(root)))
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    print("Maximum Path Sum: " + str(find_maximum_path_sum(root)))

    root = TreeNode(-1)
    root.left = TreeNode(-3)
    print("Maximum Path Sum: " + str(find_maximum_path_sum(root)))


main()
