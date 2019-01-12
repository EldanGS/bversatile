# https://leetcode.com/problems/n-ary-tree-postorder-traversal/description/

"""
1st solution; Recursion
Complexity analysis:
Time: O(N) - in worst case
Memory: O(N) - in worst case
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    result = []
    def __init__(self):
        self.result = []
    
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        for child in root.children:
            self.postorder(child)
        
        self.result.append(root.val)
        
        return self.result

"""
2nd solution; Iterative
Complexity analysis:
Time: O(N) - in worst case
Memory: O(N) - in worst case
"""
class Solution(object):
    def postorder(self, root):
        result = []
        if not root:
            return result
        
        stack = [root]
        while stack:
            node = stack.pop()
            result.append(node.val)
            stack.extend(node.children)
            
        return result[::-1]
