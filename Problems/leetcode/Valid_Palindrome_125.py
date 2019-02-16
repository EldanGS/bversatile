# https://leetcode.com/problems/valid-palindrome/description/


class Solution:
    def isPalindrome(self, s: 'str') -> 'bool':
        if not s:
            return True

        left, right = 0, len(s) - 1
        while left <= right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left, right = left + 1, right - 1

        return True
