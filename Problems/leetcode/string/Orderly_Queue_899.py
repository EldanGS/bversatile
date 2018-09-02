# https://leetcode.com/problems/orderly-queue/description/

"""
Solution.
Complexity analysis:
Time: O(NlogN) - in worst case
Memory: O(N) - in worst case
"""
class Solution:
    def orderlyQueue(self, s, k):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        return ''.join(sorted(s)) if k > 1 else min(s[i:] + s[:i] for i in range(len(s)))