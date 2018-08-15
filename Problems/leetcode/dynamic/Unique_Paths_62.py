# https://leetcode.com/problems/unique-paths/description/


"""
1st solution.
Complexity analysis:
Time: O(N*M) - in worst case
Memory: O(N*M) - in worst case
"""
class Solution:
    def uniquePaths(self, n, m):
        dp = [[1] * m for _ in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        return dp[n - 1][m - 1]
    
"""
2nd solution.
Complexity analysis:
Time: O(N*M) - in worst case
Memory: O(N) - in worst case
"""
class Solution:
    def uniquePaths(self, m, n):
        if m > n:
            self.uniquePaths(n, m)
        
        dp = [1] * m
        for j in range(1, n):
            for i in range(1, m):
                dp[i] += dp[i - 1]
        
        return dp[m - 1]
    
        