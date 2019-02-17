from test_framework import generic_test


def minimum_path_weight(triangle):
    if not triangle:
        return 0

    min_path = triangle[-1]
    for i in reversed(range(len(triangle) - 1)):
        for j in range(len(triangle[i])):
            min_path[j] = min(min_path[j], min_path[j + 1]) + triangle[i][j]

    return min_path[0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("16-08-minimum_weight_path_in_a_triangle.py",
                                       'minimum_weight_path_in_a_triangle.tsv',
                                       minimum_path_weight))
