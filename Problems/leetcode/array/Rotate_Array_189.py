# https://leetcode.com/problems/rotate-array/description/
"""
Note:
	Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
	Could you do it in-place with O(1) extra space?
"""

# O(N) by time, O(1) by space
class Solution:
    def my_swap(self, start, end, nums):
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1
    
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        self.my_swap(0, n - 1, nums)
        self.my_swap(0, k - 1, nums)
        self.my_swap(k, n - 1, nums)
       

# Easy way but, O(N) by time, O(N) by space I think.
class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums) - k
        nums[:] = nums[n:] + nums[:n]