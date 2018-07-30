# https://leetcode.com/problems/merge-two-binary-trees/description/

"""
Solution.
Used: DFS algortihm
Complexity analysis:
Time: O(N) ?
Memory: O(N) in worst case, stack memory
"""

class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 and t2:
            tree = TreeNode(t1.val + t2.val)
            tree.left = self.mergeTrees(t1.left, t2.left)
            tree.right = self.mergeTrees(t1.right, t2.right)
            return tree
        else:
            return t1 or t2
        
            
        
