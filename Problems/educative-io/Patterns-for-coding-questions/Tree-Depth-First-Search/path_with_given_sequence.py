"""
Problem Statement #
Given a binary tree and a number sequence, find if the sequence is present as a
root-to-leaf path in the given tree.

Example 1:
Sequence: [1, 9, 9]
Output: true
Explanation: The tree has a path 1 -> 9 -> 9.

"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_path_helper(node, sequence, i):
    if i == len(sequence):
        return True

    if not node:
        return False

    if node.val != sequence[i]:
        return False

    return (find_path_helper(node.left, sequence, i + 1)
            or find_path_helper(node.right, sequence, i + 1))


def find_path(root, sequence):
    if not root:
        return len(sequence) == 0

    return find_path_helper(root, sequence, 0)


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
    print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))
    print("Tree has path sequence: " + str(find_path(root, [1, 0, 5])))
    print("Tree has path sequence: " + str(find_path(root, [1, 1, 5])))


main()

