"""
https://www.educative.io/courses/grokking-the-coding-interview/xV2J7jvN1or

Problem Statement # Given a binary tree and a number ‘S’, find all paths
in the tree such that the sum of all the node values of each path equals ‘S’.
Please note that the paths can start or end at any node but all paths must
follow direction from parent to child (top to bottom).

Example 1:
S: 12
Output: 3
Explanation: There are three paths with sum '12':7 -> 5, 1 -> 9 -> 2, and 9 -> 3
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_paths(node, S, path):
    if not node:
        return 0

    path.append(node.val)
    path_count, path_sum = 0, 0

    for num in path[::-1]:
        path_sum += num
        if path_sum == S:
            path_count += 1
    path_count += find_paths(node.left, S, path)
    path_count += find_paths(node.right, S, path)
    path.pop()
    return path_count


def count_paths(root, S):
    return find_paths(root, S, [])


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has paths: " + str(count_paths(root, 11)))


main()
