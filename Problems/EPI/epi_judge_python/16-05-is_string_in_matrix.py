from test_framework import generic_test
from collections import deque


def is_pattern_contained_in_grid(grid, S):
    def is_pattern_suffix_contained_starting_at_xy(x, y, offset):
        if offset == len(S):
            return True

        if (0 <= x < len(grid) and 0 <= y < len(grid[x]) and
                grid[x][y] == S[offset] and (x, y, offset) not in previous_attempts and any(
                    is_pattern_suffix_contained_starting_at_xy(x + a, y + b, offset + 1)
                    for a, b in ((1, 0), (-1, 0), (0, 1), (0, -1))
                )):
            return True

        previous_attempts.add((x, y, offset))
        return False

    previous_attempts = set()
    return any(is_pattern_suffix_contained_starting_at_xy(i, j, 0)
               for i in range(len(grid)) for j in range(len(grid[i])))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("16-05-is_string_in_matrix.py",
                                       'is_string_in_matrix.tsv',
                                       is_pattern_contained_in_grid))
