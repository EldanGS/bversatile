from test_framework import generic_test


def number_of_ways(n, m):
    if n > m:
        n, m = m, n

    number_of_ways = [1] * m
    for i in range(1, n):
        for j in range(1, m):
            number_of_ways[j] += number_of_ways[j - 1]

    return number_of_ways[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("16-03-number_of_traversals_matrix.py",
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
