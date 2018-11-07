from test_framework import generic_test


def matrix_in_spiral_order(square_matrix):
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # (row -> i, col -> j)
    direction = i = j = 0
    spiral_order = []
    n = len(square_matrix)

    for _ in range(n * n):
        spiral_order.append(square_matrix[i][j])
        square_matrix[i][j] = -1 # mark visited points to -1
        next_i, next_j = i + moves[direction][0], j + moves[direction][1]
        if (next_i not in range(n) \
                or next_j not in range(n)) \
                or square_matrix[next_i][next_j] == -1:
            direction = (direction + 1) % 4
            next_i, next_j = i + moves[direction][0], j + moves[direction][1]
        i, j = next_i, next_j

    return spiral_order


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("5-18-spiral_ordering_segments.py",
                                       "spiral_ordering_segments.tsv",
                                       matrix_in_spiral_order))
