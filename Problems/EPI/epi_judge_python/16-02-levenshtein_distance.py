from test_framework import generic_test


def levenshtein_distance(A, B):
    if len(A) > len(B):
        A, B = B, A

    len_A, len_B = len(A) + 1, len(B) + 1
    dp = [[0] * len_B
          for _ in range(len_A)]
    for i in range(len_A):
        for j in range(len_B):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

    return dp[-1][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("16-02-levenshtein_distance.py",
                                       "levenshtein_distance.tsv",
                                       levenshtein_distance))
