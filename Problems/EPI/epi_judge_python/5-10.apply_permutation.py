from test_framework import generic_test


def apply_permutation(perm, A):
    for i in range(len(A)):
        next = i
        while perm[next] >= 0:
            A[i], A[perm[next]] = A[perm[next]], A[i]
            temp = perm[next]
            perm[next] -= len(perm)
            next = temp

    perm[:] = [a + len(perm) for a in perm]

def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("5-10.apply_permutation.py",
                                       "apply_permutation.tsv",
                                       apply_permutation_wrapper))