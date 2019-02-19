from test_framework import generic_test


def generate_pascal_triangle(n):
    pascal_triangle = [[1] * (i + 1) for i in range(n)]
    for i in range(n):
        for j in range(1, i):
            pascal_triangle[i][j] = pascal_triangle[i - 1][j - 1] + pascal_triangle[i - 1][j]

    return pascal_triangle


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("05-20-pascal_triangle.py",
                                       'pascal_triangle.tsv',
                                       generate_pascal_triangle))
