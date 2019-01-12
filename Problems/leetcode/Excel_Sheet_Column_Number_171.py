# https://leetcode.com/problems/excel-sheet-column-number/description/

"""
Solution.
Complexity analysis:
Time: O(N) - always
Memory: O(1) - in worst case
"""

class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for c in s:
            result = result * 26 + ord(c) - 64
            
        return result
