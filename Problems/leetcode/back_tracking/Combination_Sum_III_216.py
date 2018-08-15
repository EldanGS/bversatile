# https://leetcode.com/problems/combination-sum-iii/description/

"""
Solution.
Complexity analysis:
Time: O(N^2) - in worst case
Memory: O(N) - always
"""

class Solution:
    def __init__(self):
       self.result = []
    
    def dfs(self, nums, k, n, index, comb):
        if k < 0 or n < 0:
            return
        if k == 0 and n == 0:
            self.result.append(comb)
            return
        for i in range(index, len(nums)):
            self.dfs(nums, k - 1, n - nums[i], i + 1, comb + [nums[i]])
        
    def combinationSum3(self, k, n):
        self.dfs(range(1, 10), k, n, 0, [])
        return self.result;
