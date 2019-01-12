# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

"""
Solution 
Complexity analysis:
Time: O(N) - always
Memory: O(1) - always
"""
class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        duplicates = []
        
        for num in nums:
            if nums[abs(num) - 1] < 0:
                duplicates.append(abs(num))
            else:
                nums[abs(num) - 1] *= -1
            
        return duplicates
