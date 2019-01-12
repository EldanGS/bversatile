# https://leetcode.com/problems/flipping-an-image/description/

"""
Solution.
Complexity analysis:
Time: O(N²) - always
Memory: O(1) - always
"""

class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        # make a reverse each matrix rows
        # and compute Xor operation to inverting bits for values in each row
        return [[val ^ 1 for val in row[::-1]] for row in A]
