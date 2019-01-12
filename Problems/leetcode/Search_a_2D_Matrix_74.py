# https://leetcode.com/problems/search-a-2d-matrix/description/

"""
Solution.
Complexity analysis:
Time: O(NlogM) - in worst case
Memory: O(N) - in worst case
"""

class Solution:
    def check(self, left, right, arr, target):
        while left < right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return True
            if arr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return arr[left] == target
    
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        for row in matrix:
            if row[0] > target:
                continue
            if self.check(0, len(row) - 1, row, target):
                return True
        
        return False