# https://leetcode.com/problems/valid-perfect-square/description/

"""
Solution.
Complexity analysis:
Time: O(logN) - always
Memory: O(1) - always
"""

class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left, right = 1, num
        while left <= right:
            mid = left + (right - left) // 2
            
            if mid * mid == num:
                return True
            elif mid * mid > num:
                right = mid - 1
            else:
                left = mid + 1
        
        return False
