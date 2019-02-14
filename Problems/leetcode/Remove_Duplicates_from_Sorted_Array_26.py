# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        running_index = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[running_index - 1]:
                nums[running_index] = nums[i]
                running_index += 1

        return running_index
