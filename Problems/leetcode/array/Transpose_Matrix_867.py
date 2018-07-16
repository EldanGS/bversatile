# https://leetcode.com/problems/transpose-matrix/description/

"""
1st solution.
Complexity analysis:
Time: O(N²) - always
Memory: O(N²) - always
"""
class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        trans_A = []
        rows = len(A)
        cols = len(A[0])
        
        for col in range(0, cols):
            temp = []
            for row in range(0, rows):
                temp.append(A[row][col])
            trans_A.append(temp)
        
        return trans_A

"""
2nd solution more concise.
Complexity analysis:
Time: O(N²) - always
Memory: O(N²) - always
"""
class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]


"""
3th solution more tricky.
Complexity analysis:
Time: O(N²) - always
Memory: O(N²) - ?
"""
class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return zip(*A)
