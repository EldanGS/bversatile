"""
Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Examples:

Given binary tree [3,9,20,null,null,15,7],
   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7
return its vertical order traversal as:

[
  [9],
  [3,15],
  [20],
  [7]
]
Given binary tree [3,9,8,4,0,1,7],
     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
return its vertical order traversal as:

[
  [4],
  [9],
  [3,0,1],
  [8],
  [7]
]
Given binary tree [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5),
     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
    /\
   /  \
   5   2
return its vertical order traversal as:

[
  [4],
  [9,5],
  [3,0,1],
  [8,2],
  [7]
]

"""

import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def vertical_traversal(root: TreeNode):
    populate = collections.defaultdict(list)

    def dfs(node=root, state=0, depth=0):
        populate[state].append((depth, node.val))
        if node.left:
            dfs(node.left, state - 1, depth + 1)
        if node.right:
            dfs(node.right, state + 1, depth + 1)

    dfs()
    keys = list(sorted(populate.keys()))
    result = []

    for key in keys:
        populate[key].sort()
        result.append([y for x, y in populate[key]])

    return result


def vertical_traversal2(root: TreeNode):
    if not root:
        return []

    degree_map = collections.defaultdict(list)
    queue = [(root, 0)]

    while queue:
        new_queue = []
        for node, degree in queue:
            degree_map[degree].append(node.val)

            if node.left:
                new_queue.append((node.left, degree - 1))
            if node.right:
                new_queue.append((node.right, degree + 1))

        queue = new_queue

    return [degree_map[state] for state in sorted(degree_map)]


def vertical_traversal_sum(root: TreeNode):
    vertical_order = collections.defaultdict(int)
    queue = [(root, 0)]

    while queue:
        new_queue = []

        for node, state in queue:
            vertical_order[state] += node.val

            if node.left:
                new_queue.append((node.left, state - 1))
            if node.right:
                new_queue.append((node.right, state + 1))

        queue = new_queue

    return [vertical_order[state] for state in sorted(vertical_order)]


if __name__ == '__main__':
    n1 = TreeNode(4)
    n2 = TreeNode(2)
    n3 = TreeNode(1)
    n4 = TreeNode(3)
    n5 = TreeNode(6)
    n6 = TreeNode(5)
    n7 = TreeNode(7)

    n1.left = n2
    n2.left = n3
    n2.right = n4

    n1.right = n5
    n5.left = n6
    n5.right = n7

    vertical_tree = vertical_traversal_sum(n1)
    print(vertical_tree)
