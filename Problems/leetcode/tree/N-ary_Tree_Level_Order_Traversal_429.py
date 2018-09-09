# https://leetcode.com/problems/n-ary-tree-level-order-traversal/description/

"""
Solution.
Complexity analysis:
Time: O(N + M) - in worst case
Memory: O(N) - in worst case
"""

# Definition for a Node.
# class Node(object):
#     def __init__(self, val, children):
#         self.val = val
#         self.children = children

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        result, q = [], [root]
        
        while any(q):
            result.append([node.val for node in q])
            q = [child for node in q for child in node.children if child]
        
        return result
            