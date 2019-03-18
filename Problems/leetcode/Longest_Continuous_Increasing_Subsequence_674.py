# https://leetcode.com/problems/longest-continuous-increasing-subsequence/


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_sequence, count = 1, 1
        for i, num in enumerate(nums[1:], 1):
            if nums[i - 1] < num:
                count += 1
            else:
                max_sequence = max(max_sequence, count)
                count = 1

        return max(max_sequence, count)
