"""
https://leetcode.com/problems/palindromic-substrings/

Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as
different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".


Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".


Note:
The input string length won't exceed 1000.

"""


# O(N^2) by time & space
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        count = 0
        for i in range(n):
            dp[i][i] = 1
            count += 1

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = 1
                count += 1

        for dist in range(3, n + 1):
            for i in range(n - dist + 1):
                j = i + dist - 1
                if dp[i + 1][j - 1] and s[i] == s[j]:
                    dp[i][j] = 1
                    count += 1

        return count


# O(N) by time & space, Z-function or Manacher algorithm
class Solution:
    def countSubstrings(self, s: str) -> int:
        s = "@#" + '#'.join(s) + '#$'
        n = len(s)
        z = [0] * n
        l, r = 0, 0
        for i in range(1, n - 1):
            if i < r:
                z[i] = min(r - i, z[2 * l - i])
            while s[i + z[i] + 1] == s[i - z[i] - 1]:
                z[i] += 1
            if i + z[i] > r:
                l, r = i, i + z[i]

        return sum((v + 1) // 2 for v in z)
