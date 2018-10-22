# https://leetcode.com/problems/find-and-replace-pattern/description/

"""
Solution.
Complexity analysis:
Time: O(N * max(M)) - in worst case
Memory: O(N) - always
"""
class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def check(word):
            data = {}
            return [data.setdefault(c, len(data)) for c in word]
        
        p = check(pattern)
        return [word for word in words if check(word) == p]
