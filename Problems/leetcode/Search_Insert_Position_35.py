# https://leetcode.com/problems/search-insert-position/description/

"""
Solution.
Complexity analysis:
Time: O(logN) - always
Memory: O(1) - always
"""

class Solution:
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        
        return left