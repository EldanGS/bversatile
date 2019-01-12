# https://leetcode.com/problems/count-binary-substrings/description/

"""
Note:
s.length will be between 1 and 50,000.
s will only consist of "0" or "1" characters.
"""

# O(N) by time, O(1) by space
class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        prev_len = 0
        cur_len = 1
        count = 0
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cur_len += 1
            else:
                prev_len = cur_len
                cur_len = 1
            if cur_len <= prev_len:
                count += 1
        
        return count