# author: Eldan Abdrashim
# task: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def _directed_parent_connection(self, node, parent=None):
        if node:
            node.parent = parent
            self._directed_parent_connection(node.left, node)
            self._directed_parent_connection(node.right, node)

    def k_distance_nodes(self, root, target, k) -> []:
        if not root:
            return []

        self._directed_parent_connection(root)
        queue = deque([(target, 0)])
        visited_nodes = {target}
        while queue:
            if queue[0][1] == k:
                return [node.val for node, distance in queue]

            node, distance = queue.popleft()
            for neighbor in (node.left, node.right, node.parent):
                if neighbor and neighbor not in visited_nodes:
                    queue.append((neighbor, distance + 1))
                    visited_nodes.add(neighbor)

        return []


if __name__ == '__main__':
    tree = TreeNode(3)
    tree.left = TreeNode(5)
    tree.right = TreeNode(1)

    tree.left.left = TreeNode(6)
    tree.left.right = TreeNode(2)
    tree.right.left = TreeNode(0)
    tree.right.right = TreeNode(8)

    tree.left.right.left = TreeNode(7)
    tree.left.right.right = TreeNode(4)

    """
                3
              /   \
           [5]		1
          /  \    /  \
        6     2  0	  8
            /  \
           7    4	
    """
    target = tree.left
    k = 2

    solution = Solution()
    result = solution.k_distance_nodes(tree, target, k)

    if not result:
        print('There is no k distinated nodes in the tree')
    else:
        print(result)
