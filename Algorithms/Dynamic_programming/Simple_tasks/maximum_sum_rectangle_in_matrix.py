"""

Given a 2D array, find the maximum sum subarray in it. For example,
in the following 2D array.
matrix = [[2, 1, -3, -4, 5],
          [0, 6,  3, 4,  1],
          [2, -2, -1, 4, -5],
          [-3, 3, 1, 0,  3]]
answer: 18
submatrix,
        [6, 3, 4]
        [-2,-1,4]
        [3, 1, 0]
"""


def max_submatrix_in_matrix(matrix):
    max_res, has_positive = float('-inf'), False
    for row in matrix:
        for val in row:
            if val > 0:
                has_positive = True
                break
            elif max_res < val:
                max_res = val

    if not has_positive:
        return max_res

    n, m = len(matrix), len(matrix[0])
    max_sum = float('-inf')
    for l in range(m):
        col_sum = [0] * n
        for r in range(l, m):
            for i in range(n):
                col_sum[i] += matrix[i][r]

            cur_sum = get_maximum_subarray_sum(col_sum)
            if max_sum < cur_sum:
                max_sum = cur_sum
    return max_sum


def get_maximum_subarray_sum(col):
    cur_sum, min_sum, max_sum = 0, 0, float('-inf')
    for val in col:
        cur_sum += val
        if max_sum < cur_sum - min_sum:
            max_sum = cur_sum - min_sum
        if min_sum > cur_sum:
            min_sum = cur_sum

    return max_sum


if __name__ == '__main__':
    matrix = [[2, 1, -3, -4, 5],
              [0, 6,  3, 4,  1],
              [2, -2, -1, 4, -5],
              [-3, 3, 1, 0,  3]]
    print(max_submatrix_in_matrix(matrix))

