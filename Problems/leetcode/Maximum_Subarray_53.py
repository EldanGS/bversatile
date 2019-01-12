# https://leetcode.com/problems/maximum-subarray/description/

"""
Solution.
Used: Kadane algorithm
Complexity analysis:
Time: O(N)
Memory: O(1) 
"""
class Solution:
    def maxSubArray(self, nums):
        if not nums:
            return 0
        
        n = len(nums)
        prev = nums[0]
        max_sum = nums[0]
        
        for i in range(1, n):
            prev = max(nums[i], prev + nums[i])
            max_sum = max(max_sum, prev)
            
        return max_sum