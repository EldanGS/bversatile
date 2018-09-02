# https://leetcode.com/problems/bitwise-ors-of-subarrays/description/

"""
Solution.
Complexity analysis:
Time: O(30 * N) - in worst case
Memory: O(N) - in worst case
"""
class Solution:
    def subarrayBitwiseORs(self, arr):
        """
        :type A: List[int]
        :rtype: int
        """
        result, curr = set(), {0}
        for i in arr:
            curr = {i | j for j in curr} | {i}
            result |= curr
        
        return len(result)