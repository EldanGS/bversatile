# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(t):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2

                if nums[mid] >= t:
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        left_index = binary_search(target)
        right_index = binary_search(target + 1) - 1

        return [left_index, right_index] if target in nums[left_index:left_index + 1] else [-1, -1]
