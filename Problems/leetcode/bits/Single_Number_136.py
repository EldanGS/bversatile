# https://leetcode.com/problems/single-number/description/

"""
Solution.
Complexity analysis:
Time: O(N) - in worst case
Memory: O(1) - always
"""

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        single = 0
        for num in nums:
            single ^= num
            
        return single