# https://leetcode.com/problems/minimum-moves-to-equal-array-elements/description/

"""
Solution.
Complexity analysis:
Time: O(N) - always
Memory: O(1) - in worst case
"""

class Solution:
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - len(nums) * min(nums)
