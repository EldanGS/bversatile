"""
https://leetcode.com/problems/longest-palindromic-subsequence/

Given a string s, find the longest palindromic subsequence's length in s. You
may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".
Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".

"""


# O(N^2) by time & space
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if s == s[::-1]:
            return len(s)

        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1

        for dist in range(1, n):
            for i in range(n - dist):
                j = i + dist
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][-1]


# O(N^2) time, O(N) space
class Solution2:
    def longestPalindromeSubseq(self, s: str) -> int:
        if s == s[::-1]:
            return len(s)

        n = len(s)
        dp = [1] * n
        for j in range(1, n):
            prev = dp[j]
            for i in reversed(range(j)):
                temp = dp[i]
                if s[i] == s[j]:
                    dp[i] = 2 + prev if i + 1 < j else 2
                else:
                    dp[i] = max(dp[i + 1], dp[i])
                prev = temp

        return dp[0]
