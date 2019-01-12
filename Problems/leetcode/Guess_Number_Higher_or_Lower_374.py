# https://leetcode.com/problems/guess-number-higher-or-lower/description/

"""
Solution.
Complexity analysis:
Time: O(logN) - always
Memory: O(1) - always
"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        
        while True:
            mid = left + (right - left) // 2
            res = guess(mid)
            
            if res == 0:
                return mid
            elif res == 1:
                left = mid + 1
            else:
                right = mid - 1