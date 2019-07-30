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


def verticalTraversal(root: TreeNode):
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


def verticalTraversal2(root: TreeNode):
    g = collections.defaultdict(list)
    queue = [(root, 0)]

    while queue:
        new = []
        d = collections.defaultdict(list)

        for node, s in queue:
            d[s].append(node.val)
            if node.left:
                new += [(node.left, s - 1)]
            if node.right:
                new += [(node.right, s + 1)]

        for k in d:
            g[k].extend(sorted(d[k]))
        queue = new

    return [g[i] for i in sorted(g)]
