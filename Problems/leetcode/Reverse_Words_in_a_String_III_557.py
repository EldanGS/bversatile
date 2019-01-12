# https://leetcode.com/problems/reverse-words-in-a-string-iii/description/

# 1st solution, more readable
class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(word[::-1] for word in s.split())
        

# 2nd solution
class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(s.split()[::-1])[::-1]
