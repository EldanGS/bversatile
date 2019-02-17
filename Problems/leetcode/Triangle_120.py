# https://leetcode.com/problems/triangle/


class Solution:
    def minimumTotal(self, triangle: 'List[List[int]]') -> 'int':
        dp = triangle[-1]
        for i in reversed(range(len(triangle) - 1)):
            for j in range(len(triangle[i])):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]

        return dp[0]
   