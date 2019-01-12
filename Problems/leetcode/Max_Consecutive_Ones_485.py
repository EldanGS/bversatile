# https://leetcode.com/problems/max-consecutive-ones/description/

"""
Solution.
Complexity analysis:
Time: O(N) - always
Memory: O(1) - always
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        max_count = 0
        for num in nums:
            if num:
                count += 1
            else:
                count = 0
            max_count = max(max_count, count)
        
        return max_count

