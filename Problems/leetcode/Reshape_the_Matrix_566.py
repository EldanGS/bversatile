# https://leetcode.com/problems/reshape-the-matrix/description/


"""
Solution.
Complexity analysis:
Time: O(N²) - always
Memory: O(N²) - always
"""
class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        n = len(nums)
        m = len(nums[0])
        elements = n * m
        if r * c != elements:
            return nums
        
        matrix = [[0 for i in range(c)] for j in range(r)]
        for i in range(elements):
            matrix[i // c][i % c] = nums[i // m][i % m]
        
        return matrix
