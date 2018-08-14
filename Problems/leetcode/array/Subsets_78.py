# https://leetcode.com/problems/subsets/description/

"""
1st solution, recursively
Complexity analysis:
Time: O(2^N) - in worst case
Memory: O(N^2) - in worst case
"""

class Solution:
    def __init__(self):
       self.result = []
    
    def dfs(self, nums, path):
        self.result.append(path)
        for i in range(len(nums)):
            self.dfs(nums[i + 1:], path + [nums[i]])
        
        return self.result
    
    def subsets(self, nums):
        result, path = [], []
        self.dfs(nums, path)
        return self.result


"""
2nd solution, iteratively
Complexity analysis:
Time: O(2^N) - in worst case
Memory: O(N^2) - in worst case
"""

class Solution:
    def subsets(self, nums):
        result = [[]]
        for num in nums:
            result += [item + [num] for item in result]
        
        return result
    
        
        