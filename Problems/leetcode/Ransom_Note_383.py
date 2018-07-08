# https://leetcode.com/problems/ransom-note/description/

# 1st solution: O(N + M) by time, O(const) by space
class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        data = dict()
        for c in magazine:
            if data.get(c):
                data[c] += 1
            else:
                data[c] = 1
        
        for c in ransomNote:
            if not data.get(c) or data[c] < 0:
                return False
            data[c] -= 1
        
        return True

# 2nd solution elegant: O(N + M) by time, O(const) by space
class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        return not collections.Counter(ransomNote) - collections.Counter(magazine)

