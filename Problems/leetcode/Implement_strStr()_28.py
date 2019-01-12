# https://leetcode.com/problems/implement-strstr/description/

# hard implementation, O(N * M) by time, O(1) by space
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        len_n = len(needle)
        len_h = len(haystack)
        
        i = 0
        while True:
            j = 0
            while True:
                if j == len_n:
                    return i
                if i + j == len_h:
                    return -1
                if haystack[i + j] != needle[j]:
                    break
                j += 1
            i += 1
            
        return 0
        

# elegant implement, O(N * M * const) by time, O(1) by space
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        len_n = len(needle)
        len_h = len(haystack)
        
        if not len_n:
            return 0
        for i in range(len_h):
            if haystack[i: i + len_n] == needle:
                return i
            
        return -1


# Optimal solution with KMP algorithm, O(N + M) by time, O(N) by space
class Solution:
    def KMP(self, s):
        j, prefix = 0, [0]
        for i in range(1, len(s)):
            while j > 0 and s[i] != s[j]:
                j = prefix[j - 1]
            if s[i] == s[j]:
                j += 1
            else:
                j = 0
            prefix.append(j)
        
        return prefix
            
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        prefix = self.KMP(needle + '#' + haystack)
        n = len(needle)
        
        if not n:
            return 0
        for i in range(n + 1, len(prefix)):
            if prefix[i] == n:
                return i - 2 * n
        
        return -1
        