# https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total = n * (n + 1) // 2
        return (total - sum(nums))
        