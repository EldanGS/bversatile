# https://leetcode.com/problems/reverse-string/description/

# O(N) by time, O(N) by space cause transform to list
class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        
        return ''.join(s)
        

# elegant pythonic, O(N) by time, O(1) by space?
class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]
