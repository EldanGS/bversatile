# https://leetcode.com/problems/array-nesting/description/

"""
Solution.
Complexity analysis:
Time: O(N) - in worst case
Memory: O(1) - always
"""

class Solution:
    def arrayNesting(self, nums):
        max_nested = 0
        n = len(nums)
        
        for i in range(n):
            current_nested = 0
            k = i
            
            while nums[k] >= 0:
                temp = nums[k]
                nums[k] = -1
                k = temp
                
                current_nested += 1
            
            max_nested = max(max_nested, current_nested)
        
        return max_nested
