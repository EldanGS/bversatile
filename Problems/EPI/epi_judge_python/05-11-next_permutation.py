from test_framework import generic_test


def next_permutation(perm):
    inversion_point = len(perm) - 2
    while inversion_point >= 0 and perm[inversion_point] >= perm[inversion_point + 1]:
        inversion_point -= 1

    if inversion_point == -1:
        return []

    for i in reversed(range(inversion_point + 1, len(perm))):
        if perm[i] > perm[inversion_point]:
            perm[i], perm[inversion_point] = perm[inversion_point], perm[i]
            break

    perm[inversion_point + 1:] = reversed(perm[inversion_point + 1:])
    return perm


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "05-11-next_permutation.py", 'next_permutation.tsv', next_permutation))
