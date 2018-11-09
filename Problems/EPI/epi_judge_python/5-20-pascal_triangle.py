from test_framework import generic_test


def generate_pascal_triangle(n):
    triangle = [[1] * (i + 1) for i in range(n)]
    for i in range(n):
        for j in range(1, i):
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

    return triangle


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("5-20-pascal_triangle.py",
                                       'pascal_triangle.tsv',
                                       generate_pascal_triangle))
