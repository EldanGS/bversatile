# https://leetcode.com/problems/toeplitz-matrix/description/

"""
1st solution.
Complexity analysis:
Time: O(N) - always
Memory: O(1) - always
"""
class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        rows = len(matrix)
        cols = len(matrix[0])
        
        for i in range(0, rows - 1):
            for j in range(0, cols - 1):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
        
        return True

"""
2nd solution, more
Complexity analysis:
Time: O(N) - always
Memory: O(1) - always
"""    
class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        return all(matrix[i][j] == matrix[i + 1][j + 1] for i in range(len(matrix) - 1) for j in range(len(matrix[0]) - 1))