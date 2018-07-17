# https://leetcode.com/problems/house-robber/description/

"""
Solution.
Complexity analysis:
Time: O(N)
Memory: O(1) 
"""
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: 
            return 0
        
        n = len(nums)
        even_sum = 0
        odd_sum = 0
        
        for i in range(n):
            if i & 1:
                odd_sum = max(even_sum, odd_sum + nums[i])
            else:
                even_sum = max(odd_sum, even_sum + nums[i])
        
        return max(even_sum, odd_sum)