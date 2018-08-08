# https://leetcode.com/problems/number-complement/description/

"""
Solution.
Complexity analysis:
Time: O(logN) - in worst case
Memory: O(1) - always
"""

class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        mask = ~0
        while mask & num:
            mask <<= 1
        
        return ~mask & ~num


