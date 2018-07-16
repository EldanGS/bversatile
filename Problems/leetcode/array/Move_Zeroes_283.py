# https://leetcode.com/problems/move-zeroes/description/

"""
Solution.
Complexity analysis:
Time: O(N) - always
Memory: O(1) - always
"""
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        try:
            zero_index = nums.index(0)
        except ValueError:
            return
        else:
	        zero = 0
	        for i in range(len(nums)):
	            if nums[i] and zero <= i:
	                nums[i], nums[zero] = nums[zero], nums[i]
	                zero += 1
        
        
