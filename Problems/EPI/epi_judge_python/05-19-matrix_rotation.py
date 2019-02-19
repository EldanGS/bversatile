from test_framework import generic_test


def rotate_matrix(square_matrix):
    n = len(square_matrix) - 1
    for i in range((n + 1) // 2):
        for j in range(i, n - i):
            (square_matrix[i][j], square_matrix[~j][i], square_matrix[~i][~j], square_matrix[j][~i]) = (
                square_matrix[~j][i], square_matrix[~i][~j], square_matrix[j][~i], square_matrix[i][j])


def rotate_matrix_wrapper(square_matrix):
    rotate_matrix(square_matrix)
    return square_matrix


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("05-19-matrix_rotation.py",
                                       'matrix_rotation.tsv',
                                       rotate_matrix_wrapper))
