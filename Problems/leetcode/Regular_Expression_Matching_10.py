# https://leetcode.com/problems/regular-expression-matching/

# O(N * M) time and space
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        n, m = len(s), len(p)
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True

        for i in range(m):
            if p[i] == '*' and dp[0][i - 1]:
                dp[0][i + 1] = True

        for i in range(n):
            for j in range(m):
                if p[j] == '*':
                    if p[j - 1] != s[i] and p[j - 1] != '.':
                        dp[i + 1][j + 1] = dp[i + 1][j - 1]
                    else:
                        dp[i + 1][j + 1] = dp[i + 1][j] or dp[i][j + 1] or dp[i + 1][j - 1]
                else:
                    dp[i + 1][j + 1] = dp[i][j] and (s[i] == p[j] or p[j] == '.')
        return dp[-1][-1]
