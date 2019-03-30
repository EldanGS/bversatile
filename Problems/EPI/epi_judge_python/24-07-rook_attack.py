import copy

from test_framework import generic_test


def rook_attack(A):
    n, m = len(A), len(A[0])
    has_first_row_zero = 0 in A[0]
    has_first_column_zero = any(not A[i][0] for i in range(n))

    for i in range(1, n):
        for j in range(1, m):
            if not A[i][j]:
                A[i][0] = A[0][j] = 0

    for i in range(1, n):
        if not A[i][0]:
            for j in range(1, m):
                A[i][j] = 0

    for j in range(1, m):
        if not A[0][j]:
            for i in range(1, n):
                A[i][j] = 0

    if has_first_row_zero:
        for j in range(m):
            A[0][j] = 0

    if has_first_column_zero:
        for i in range(n):
            A[i][0] = 0


def rook_attack_wrapper(A):
    a_copy = copy.deepcopy(A)
    rook_attack(a_copy)
    return a_copy


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("24-07-rook_attack.py", 'rook_attack.tsv',
                                       rook_attack_wrapper))
