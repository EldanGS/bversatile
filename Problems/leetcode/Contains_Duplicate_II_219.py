# https://leetcode.com/problems/contains-duplicate-ii/description/

"""
Solution.
Complexity analysis:
Time: O(N) - always
Memory: O(N) - in worst case
"""
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        data = dict()
        for i, val in enumerate(nums):
            if data.get(val):
                if i - data[val] < k:
                    return True
                
            data[val] = i + 1
        
            
        return False