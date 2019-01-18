from test_framework import generic_test


def longest_nondecreasing_subsequence_length(A):
    max_length = [1] * len(A)
    for i in range(1, len(A)):
        for j in range(i):
            if A[j] <= A[i] and max_length[i] < max_length[j] + 1:
                max_length[i] = max_length[j] + 1
    return max(max_length)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "16-12-longest_nondecreasing_subsequence.py",
            'longest_nondecreasing_subsequence.tsv',
            longest_nondecreasing_subsequence_length))
