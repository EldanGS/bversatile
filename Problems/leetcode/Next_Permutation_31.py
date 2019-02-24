# https://leetcode.com/problems/next-permutation/


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot_index = len(nums) - 2
        while pivot_index >= 0 and nums[pivot_index + 1] <= nums[pivot_index]:
            pivot_index -= 1

        if pivot_index == -1:
            nums.reverse()
            return

        for i in reversed(range(pivot_index + 1, len(nums))):
            if nums[i] > nums[pivot_index]:
                nums[i], nums[pivot_index] = nums[pivot_index], nums[i]
                break

        nums[pivot_index + 1:] = reversed(nums[pivot_index + 1:])
