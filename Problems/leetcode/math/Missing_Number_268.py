# https://leetcode.com/problems/missing-number/


"""
Solution.
Complexity analysis:
Time: O(N) - always
Memory: O(1) - in worst case
"""

class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total = n * (n + 1) // 2
        return (total - sum(nums))
        