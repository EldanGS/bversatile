"""
This problem was asked by Google.

The edit distance between two strings refers to the minimum number of character insertions, deletions, and
substitutions required to change one string to the other.

For example, the edit distance between “kitten” and “sitting” is three:
substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.
"""

# O(NM) time, O(NM) space
def min_distance(word1, word2):
    n, m = len(word1) + 1, len(word2) + 1
    dp = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        dp[i][0] = i
    for j in range(m):
        dp[0][j] = j
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + (word1[i - 1] != word2[j - 1]))

    return dp[-1][-1]


# O(NM) time, O(N) space
def min_distance2(word1, word2):
    n, m = len(word1) + 1, len(word2) + 1
    pre = [j for j in range(m)]
    for i in range(n):
        cur = [i] * m
        for j in range(1, m):
            cur[j] = min(cur[j - 1] + 1, pre[j] + 1, pre[j - 1] + (word1[i - 1] != word2[j - 1]))
        pre = cur[:]

    return pre[-1]


if __name__ == '__main__':
    word1 = 'kitten'
    word2 = 'sitting'

    print(min_distance2(word1, word2))
