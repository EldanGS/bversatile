# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/

"""
Solution.
Complexity analysis:
Time: O(N) - always
Memory: O(1) - always
"""
class Solution:
    def minAddToMakeValid(self, s):
        """
        :type S: str
        :rtype: int
        """
        if not s:
            return 0
        
        left, result = 0, 0
        for c in s: 
            if c == '(':
                left += 1
            else:
                if left == 0:
                    result += 1
                else:
                    left -= 1
        
        result += left
        return result
