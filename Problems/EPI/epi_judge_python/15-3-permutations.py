from test_framework import generic_test, test_utils


def permutations(A):
    def helper(i):
        if i == len(A) - 1:
            result.append(A.copy())
            return
        for j in range(i, len(A)):
            A[i], A[j] = A[j], A[i]
            helper(i + 1)
            A[i], A[j] = A[j], A[i]

    result = []
    helper(0)

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("15-3-permutations.py", 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
