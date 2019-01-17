from test_framework import generic_test


# My solution
def minimum_path_weight1(triangle):
    if not triangle:
        return 0
    dp = triangle[-1]
    for i in reversed(range(len(triangle) - 1)):
        for j in range(len(triangle[i])):
            dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]

    return dp[0]


# Author solution
def minimum_path_weight(triangle):
    min_weight_to_curr_now = [0]
    for row in triangle:
        min_weight_to_curr_now = [row[j] +
                                  min(min_weight_to_curr_now[max(j - 1, 0)],
                                      min_weight_to_curr_now[min(j, len(min_weight_to_curr_now) - 1)])
                                  for j in range(len(row))]
    return min(min_weight_to_curr_now)


if __name__ == '__main__':
    # print(minimum_path_weight([[2], [4, 4], [8, 5, 6], [4, 2, 6, 2], [1, 5, 2, 3, 4]]))
    exit(
        generic_test.generic_test_main("16-08-minimum_weight_path_in_a_triangle.py",
                                       'minimum_weight_path_in_a_triangle.tsv',
                                       minimum_path_weight))
