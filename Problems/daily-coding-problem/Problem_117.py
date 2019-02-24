"""
This problem was asked by Facebook.

Given a binary tree, return the level of the tree with minimum sum.

"""
import collections


class Node:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

    def __repr__(self):
        return "{}=(l={}, r={})".format(self.val, self.left, self.right)


def min_level_sum(root):
    if not root:
        return 0

    queue = collections.deque([root])
    result = root.val

    while queue:
        level = len(queue)
        level_sum = 0

        for _ in range(level):
            node = queue.popleft()
            level_sum += node.val

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result = min(result, level_sum)

    return result


if __name__ == '__main__':
    """
                      4
                    /   \
                   2    -5
                  / \    /\
                -1   3 -2  6
    """
    root = Node(4)
    root.left = Node(2)
    root.right = Node(-5)
    root.left.left = Node(-1)
    root.left.right = Node(3)
    root.right.left = Node(-2)
    root.right.right = Node(6)

    print(min_level_sum(root))
