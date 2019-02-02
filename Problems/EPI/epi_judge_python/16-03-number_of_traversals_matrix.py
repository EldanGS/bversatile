from test_framework import generic_test


def number_of_ways(n, m):
    dp = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[-1][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("16-03-number_of_traversals_matrix.py",
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
