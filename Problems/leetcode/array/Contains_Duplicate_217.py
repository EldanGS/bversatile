# https://leetcode.com/problems/contains-duplicate/description/

"""
1st solution.
Complexity analysis:
Time: O(N) - always
Memory: O(N) - worst case
"""
class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        data = set()
        for num in nums:
            if num in data:
                return True
            data.add(num)
            
        return False

"""
2nd solution, more concise
Complexity analysis:
Time: O(N) - always
Memory: O(N) - worst case
"""
class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(num) != len(set(nums))