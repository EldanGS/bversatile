# https://leetcode.com/problems/first-unique-character-in-a-string/description/

# 1st solution: O(N^2) by time, O(1) by space
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i, c in enumerate(s):
            unique = True
            for j, k in enumerate(s):
                if i == j:
                    continue
                if c == k:
                    unique = False
                    break
            if unique:
                return i
        
        return -1


# 2nd solution: O(N) by time, O(1) by space
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        data = dict()
        for c in s:
            if not data.get(c):
                data[c] = 1
            else:
                data[c] += 1
        
        for index, c in enumerate(s):
            if data[c] == 1:
                return index
        
        return -1

# 3th solution elegant?: O(N * 26 ~ NlogN), O(1) by space
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = set(s)
        return min([s.index(char) for char in chars if s.count(char) == 1] or [-1])
