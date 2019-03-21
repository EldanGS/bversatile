from test_framework import generic_test


def compute_binomial_coefficient(n, k):
    C = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            if j == 0 or j == i:
                C[i][j] = 1
            else:
                C[i][j] = C[i - 1][j - 1] + C[i - 1][j]

    return C[-1][-1]


def compute_binomial_coefficient2(n, k):
    C = [1] + [0] * k
    for i in range(1, n + 1):
        for j in range(min(i, k), -1, -1):
            C[j] += C[j - 1]

    return C[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("16-04-binomial_coefficients.py",
                                       'binomial_coefficients.tsv',
                                       compute_binomial_coefficient))
