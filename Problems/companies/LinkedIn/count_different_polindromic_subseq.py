"""
link: https://leetcode.com/problems/count-different-palindromic-subsequences/

Given a string S, find the number of different non-empty palindromic
subsequences in S, and return that number modulo 10^9 + 7.

A subsequence of a string S is obtained by deleting 0 or more characters from S.

A sequence is palindromic if it is equal to the sequence reversed.

Two sequences A_1, A_2, ... and B_1, B_2, ... are different if there is some
i for which A_i != B_i.

Example 1:

Input:
S = 'bccb'
Output: 6
Explanation:
The 6 different non-empty palindromic subsequences are 'b', 'c', 'bb', 'cc', 'bcb', 'bccb'.
Note that 'bcb' is counted only once, even though it occurs twice.
Example 2:

Input: S = 'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'
Output: 104860361 Explanation: There are 3104860382 different non-empty
palindromic subsequences, which is 104860361 modulo 10^9 + 7. Note:

The length of S will be in the range [1, 1000].
Each character S[i] will be in the set {'a', 'b', 'c', 'd'}.
"""


# O(N^2) by time & space
class Solution:
    MOD = 10 ** 9 + 7

    def dfs(self, S, start, end, memo, upper, lower):
        if start > end:
            return 0
        elif start == end:
            return 1
        elif memo[start][end] != -1:
            return memo[start][end]

        count = 0
        for k in range(4):
            new_start, new_end = upper[k][start], lower[k][end]
            if new_start == -1 or new_start > end:
                continue

            count += 1
            if new_start != new_end:
                count += 1
            count += self.dfs(S, new_start + 1, new_end - 1, memo, upper, lower)

        memo[start][end] = count
        if memo[start][end] > self.MOD:
            memo[start][end] %= self.MOD

        return memo[start][end]

    def countPalindromicSubsequences(self, S: str) -> int:
        if not S:
            return 0

        n = len(S)
        memo = [[-1] * n for _ in range(n)]
        upper = [[-1] * n for _ in range(4)]
        for i in reversed(range(n)):
            code = ord(S[i]) - ord('a')
            for k in range(4):
                if k == code:
                    upper[k][i] = i
                elif i < n - 1:
                    upper[k][i] = upper[k][i + 1]
        lower = [[-1] * n for _ in range(4)]
        for i in range(n):
            code = ord(S[i]) - ord('a')
            for k in range(4):
                if k == code:
                    lower[k][i] = i
                elif i > 0:
                    lower[k][i] = lower[k][i - 1]

        return self.dfs(S, 0, n - 1, memo, upper, lower)
