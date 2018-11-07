from test_framework import generic_test


def next_permutation(perm):
    n = len(perm) - 1
    pos, pivot = -1, -1
    for i in reversed(range(n)):
        if perm[i] < perm[i + 1]:
            pos = i
            pivot = perm[i]
            break

    if pos == -1:
        return []

    for i in reversed(range(n + 1)):
        if perm[i] > pivot:
            perm[i], perm[pos] = perm[pos], perm[i]
            break

    perm[pos + 1:] = reversed(perm[pos + 1:])

    return perm


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "5-11-next_permutation.py", 'next_permutation.tsv', next_permutation))
