# https://leetcode.com/discuss/interview-question/347374/Google-and-Facebook-or-Onsite-or-Verify-Binary-Tree

"""
Given a list of TreeNodes. TreeNode is standard LC class:

class TreeNode {
    TreeNode left;
    TreeNode right;
    int val;
}
Find out if all these nodes belong to the same valid binary tree.

public boolean isBinaryTree(List<TreeNode> nodes) {
}
Example 1:

Let's say we have the following binary tree

		1
       ↙ ↘
      2   3
         ↙
        4

We can create it like this
TreeNode n1 = new TreeNode(1);
TreeNode n2 = new TreeNode(2);
TreeNode n3 = new TreeNode(3);
TreeNode n4 = new TreeNode(4);

n1.left = n2;
n1.right = n3;
n3.left = n4;

Input: [n4, n2, n3, n1]
Output: true
Example 2:

		 1
       ↙  ↘
      2    3
       ↘  ↙
        4

TreeNode n1 = new TreeNode(1);
TreeNode n2 = new TreeNode(2);
TreeNode n3 = new TreeNode(3);
TreeNode n4 = new TreeNode(4);

n1.left = n2;
n1.right = n3;
n2.right = n4;
n3.left = n4;

Input: [n2, n3, n4, n1]
Output: false
Example 3:

	 1
	⤤ ⤦
	 2

TreeNode n1 = new TreeNode(1);
TreeNode n2 = new TreeNode(2);

n1.left = n2;
n2.left = n1;

Input: [n1, n2]
Output: false
Example 4:

		1           4
       ↙ ↘        ↙  ↘
      2   3      5     6

TreeNode n1 = new TreeNode(1);
TreeNode n2 = new TreeNode(2);
TreeNode n3 = new TreeNode(3);
TreeNode n4 = new TreeNode(4);
TreeNode n5 = new TreeNode(5);
TreeNode n6 = new TreeNode(6);

n1.left = n2;
n1.right = n3;

n4.left = n5;
n4.right = n6;

Input: [n2, n6, n4, n1, n3, n5]
Output: false
Example 5:

		1
       ↙ ↘
      2   3
         ↙
        4

TreeNode n1 = new TreeNode(1);
TreeNode n2 = new TreeNode(2);
TreeNode n3 = new TreeNode(3);
TreeNode n4 = new TreeNode(4);

n1.left = n2;
n1.right = n3;
n3.left = n4;

Input: [n2, n3, n1]
Output: false
Explanation: l4 is a part of the tree but it's missing in the input list so return false.
NOTE: Node values only used for demonstration purposes.

"""
from collections import defaultdict


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def valid_btree(u, graph, visited):
    if u in visited:
        return False

    visited.add(u)

    for v in graph[u]:
        if v not in visited:
            valid_btree(v, graph, visited)

    return True


def is_binary_tree(nodes):
    if not nodes:
        return True

    graph = defaultdict(list)
    indegree, outdegree = defaultdict(int), defaultdict(int)
    for node in nodes:
        outdegree[node] += 1
        indegree.setdefault(node, 0)

        if node.left:
            graph[node].append(node.left)
            indegree[node.left] += 1

        if node.right:
            graph[node].append(node.right)
            indegree[node.right] += 1

    if (any(degree > 1 for degree in indegree.values()) or
            any(degree > 2 for degree in outdegree.values())):
        return False

    visited = set()
    for node in nodes:
        if not valid_btree(node, graph, visited):
            return False

    root = 0
    for degree in indegree.values():
        if not degree:
            root += 1

    return root == 1


if __name__ == '__main__':
    """
    Let's say we have the following binary tree

		1
       ↙ ↘
      2   3
         ↙
        4

    We can create it like this
    TreeNode n1 = new TreeNode(1);
    TreeNode n2 = new TreeNode(2);
    TreeNode n3 = new TreeNode(3);
    TreeNode n4 = new TreeNode(4);
    """
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)

    n1.left = n2
    n1.right = n3
    n3.left = n4

    nodes = [n4, n2, n3, n1]
    print(is_binary_tree(nodes))
