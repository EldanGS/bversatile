from test_framework import generic_test
import math


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment):
    def has_duplicate(line):
        line = list(filter(lambda x: x != 0, line))
        return len(line) != len(set(line))

    n = len(partial_assignment)
    if any(has_duplicate([partial_assignment[i][j] for j in range(n)]) or
           has_duplicate([partial_assignment[j][i] for j in range(n)])
           for i in range(n)):
        return False

    block = int(math.sqrt(n))
    return all(not has_duplicate([
        partial_assignment[i][j]
        for i in range(block * I, block * (I + 1))
        for j in range(block * J, block * (J + 1))
    ]) for I in range(block) for J in range(block))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("05-17-is_valid_sudoku.py",
                                       "is_valid_sudoku.tsv", is_valid_sudoku))
