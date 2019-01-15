from test_framework import generic_test


def n_queens(n):
    result, col_placement = [], [0] * n

    def solve_n_queens(row):
        if row == n:
            result.append(list(col_placement))
            return
        for col in range(n):
            if all(abs(c - col) not in (0, row - i)
                   for i, c in enumerate(col_placement[:row])):
                col_placement[row] = col
                solve_n_queens(row + 1)

    solve_n_queens(0)
    return result


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("15-2-n_queens.py", 'n_queens.tsv', n_queens,
                                       comp))
