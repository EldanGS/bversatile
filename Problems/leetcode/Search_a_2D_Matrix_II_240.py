# https://leetcode.com/problems/search-a-2d-matrix-ii/description/

"""
Solution.
Complexity analysis:
Time: O(N + M) - in worst case
Memory: O(1) - always
"""

class Solution:
    def check(self, matrix, i, j, target):
        if i >= len(matrix) or j < 0:
            return False
        if matrix[i][j] == target:
            return True
        else:
            if matrix[i][j] < target:
                return self.check(matrix, i + 1, j, target)
            else:
                return self.check(matrix, i, j - 1, target)
        
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        
        return self.check(matrix, 0, len(matrix[0]) - 1, target)