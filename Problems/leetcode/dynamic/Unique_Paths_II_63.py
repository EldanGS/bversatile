# https://leetcode.com/problems/unique-paths-ii/description/

"""
Solution.
Complexity analysis:
Time: O(N*M) - always
Memory: O(N*M) - const
"""
class Solution:
    def uniquePathsWithObstacles(self, matrix):
        n, m = len(matrix), len(matrix[0])
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        dp[0][1] = 1
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if not matrix[i - 1][j - 1]:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        return dp[n][m]
