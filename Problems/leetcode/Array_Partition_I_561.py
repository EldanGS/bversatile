# https://leetcode.com/problems/array-partition-i/description/

"""
1st solution.
Complexity analysis:
Time: O(N) - always
Memory: O(1) - always
"""

class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        max_sum = 0
        for i in range(0, len(nums), 2):
            max_sum += min(nums[i], nums[i + 1])
        
        return max_sum


"""
2nd solution, more concise
Complexity analysis:
Time: O(N) - always
Memory: O(1) - always
"""

class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums)[::2])
