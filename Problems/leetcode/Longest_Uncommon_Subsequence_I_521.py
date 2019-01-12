# https://leetcode.com/problems/longest-uncommon-subsequence-i/description/

class Solution:
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        return (-1 if a == b else max(len(a), len(b)))
