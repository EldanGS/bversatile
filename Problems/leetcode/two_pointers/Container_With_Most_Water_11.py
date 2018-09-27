# https://leetcode.com/problems/container-with-most-water/description/

"""
Solution.
Complexity analysis:
Time: O(N) - in worst case
Memory: O(1) - always
"""
class Solution:
    def maxArea(self, a):
        n = len(a)
        i, j = 0, n - 1
        max_area = 0

        while i < j:
            h = min(a[i], a[j])
            max_area = max(max_area, (j - i) * h)

            while a[i] <= h and i < j:
                i += 1
            while a[j] <= h and i < j:
                j -= 1
        
        return max_area
