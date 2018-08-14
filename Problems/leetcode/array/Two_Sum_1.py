# https://leetcode.com/problems/two-sum/description/

"""
Solution.
Complexity analysis:
Time: O(N) - in worst case
Memory: O(N) - in worst case
"""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        data = {}
        result = []
        
        for i, num in enumerate(nums):
            temp = target - num
            if temp in data:
                result.append(data[temp])
                result.append(i)
                break
            
            data[num] = i
                
        return result