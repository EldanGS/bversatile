# https://leetcode.com/problems/maximum-binary-tree/

"""
Solution.
Used: DFS algorithm
Complexity analysis:
Time: O(N^2)
Memory: O(N) 
"""
class Solution:
    def constructMaximumBinaryTree(self, nums):
        if nums:
            pos = nums.index(max(nums))
            root = TreeNode(nums[pos])
            root.left = self.constructMaximumBinaryTree(nums[:pos])
            root.right = self.constructMaximumBinaryTree(nums[pos + 1:])
            
            return root
            