from test_framework import generic_test


# My solution
def number_of_ways1(n, m):
    if n > m:
        n, m = m, n
    dp = [[0] * m
          for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if i == 0:
                dp[i][j] = 1
            elif j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[-1][-1]


# Author solution
def number_of_ways(n, m):
    def compute_number_of_ways(x, y):
        if x == y == 0:
            return 1
        if number_of_ways[x][y] == 0:
            ways_top = 0 if x == 0 else compute_number_of_ways(x - 1, y)
            ways_left = 0 if y == 0 else compute_number_of_ways(x, y - 1)
            number_of_ways[x][y] = ways_left + ways_top
        return number_of_ways[x][y]

    number_of_ways = [[0] * m for _ in range(n)]
    return compute_number_of_ways(n - 1, m - 1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("16-03-number_of_traversals_matrix.py",
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
