# https://leetcode.com/problems/find-the-difference/description/

"""
Solution.
Complexity analysis:
Time: O(N + M) - in worst case
Memory: O(1) - always
"""

class Solution:
    def findTheDifference(self, s, t):
        element = 0
        for c in s:
            element ^= ord(c)
        for c in t:
            element ^= ord(c)
        
        return chr(element)