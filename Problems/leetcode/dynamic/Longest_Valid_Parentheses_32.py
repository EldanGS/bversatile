# https://leetcode.com/problems/longest-valid-parentheses/description/

"""
Solution.
Complexity analysis:
Time: O(N) - always
Memory: O(N) - in worst case
"""

class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [-1]
        result = 0
        
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    result = max(result, i - stack[-1])
                else:
                    stack.append(i)
        
        return result
