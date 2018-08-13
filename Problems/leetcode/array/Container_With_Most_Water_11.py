# https://leetcode.com/problems/container-with-most-water/description/

"""
Solution.
Complexity analysis:
Time: O(N) - always
Memory: O(1) - always
"""

class Solution:
    def maxArea(self, height):
        max_area = 0
        i, j = 0, len(height) - 1
        
        while i < j:
            current = min(height[i], height[j])
            max_area = max(max_area, (j - i) * current)
            
            if height[i] <= current:
                i += 1
            else:
                j -= 1
        
        return max_area
