# https://leetcode.com/problems/hamming-distance/description/

"""
Solution.
Complexity analysis:
Time: O(1) - ?
Memory: O(1) - ?
"""

class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x ^ y).count('1')
        
