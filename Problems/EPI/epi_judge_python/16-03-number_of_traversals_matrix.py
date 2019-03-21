from test_framework import generic_test


def number_of_ways(n, m):
    if n > m:
        n, m = m, n

    dp = [1] * n
    for i in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j - 1]

    return dp[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("16-03-number_of_traversals_matrix.py",
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
