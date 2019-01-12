# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

"""
Solution.
Complexity analysis:
Time: O(N) - always
Memory: O(N) - always
"""
class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for num in nums:
            val = abs(num) - 1
            if nums[val] > 0:
                nums[val] = -nums[val]
        
        for i, num in enumerate(nums):
            if num > 0:
                result.append(i + 1)
        return result