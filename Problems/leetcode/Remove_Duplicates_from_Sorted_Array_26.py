# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        n = len(nums)
        size = 1
        for i in range(1, n):
            if nums[i] != nums[size - 1]:
                nums[size] = nums[i]
                size += 1
        
        return size
        
                