"""https://leetcode.com/problems/closest-binary-search-tree-value-ii/ Given a
non-empty binary search tree and a target value, find k values in the BST
that are closest to the target.

Note:

Given target value is a floating point. You may assume k is always valid,
that is: k ≤ total nodes. You are guaranteed to have only one unique set of k
values in the BST that are closest to the target. Example:

Input: root = [4,2,5,1,3], target = 3.714286, and k = 2

    4
   / \
  2   5
 / \
1   3

Output: [4,3] Follow up: Assume that the BST is balanced, could you solve it
in less than O(n) runtime (where n = total nodes)?

"""
import collections
import heapq


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# O(NlogK)
class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> list
        queue = collections.deque([root])
        closest_k = []

        while queue:
            node = queue.popleft()

            diff = abs(target - node.val)
            heapq.heappush(closest_k, (-diff, node.val))
            if len(closest_k) > k:
                heapq.heappop(closest_k)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return [node[1] for node in closest_k]


# O(klogN)
class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> list:
        predecessor, successor = [], []
        curr = root
        while curr:
            if target <= curr.val:
                successor.append(curr)
                curr = curr.left
            else:
                predecessor.append(curr)
                curr = curr.right

        result = []
        while k:
            if not successor and not predecessor:
                break
            elif not successor:
                result.append(self._get_predecessor(predecessor))
            elif not predecessor:
                result.append(self._get_successor(successor))
            elif abs(successor[-1].val - target) <= abs(
                    predecessor[-1].val - target):
                result.append(self._get_successor(successor))
            else:
                result.append(self._get_predecessor(predecessor))
            k -= 1

        return result

    def _get_successor(self, nodes):
        node = nodes.pop()
        p = node.right
        while p:
            nodes.append(p)
            p = p.left
        return node.val

    def _get_predecessor(self, nodes):
        node = nodes.pop()
        p = node.left
        while p:
            nodes.append(p)
            p = p.right
        return node.val
