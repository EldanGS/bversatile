# https://leetcode.com/problems/valid-parentheses/


# O(N) time, O(N) space
class Solution:
    def isValid(self, s: 'str') -> 'bool':
        parentheses = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for c in s:
            if c in parentheses:
                stack.append(parentheses[c])
            elif not stack or stack.pop() != c:
                return False

        return not stack
