from test_framework import generic_test
from bisect import bisect_right


# O(N^2) time, O(N) space
def longest_nondecreasing_subsequence_length2(A):
    n = len(A)
    max_length = [1] * n

    for i in range(n):
        for j in range(i):
            if A[j] <= A[i]:
                max_length[i] = max(max_length[i], max_length[j] + 1)

    return max(max_length)


# O(NlogN) time, O(N) space
def longest_nondecreasing_subsequence_length(A):
    n = len(A)
    max_length = [float('inf')] * (n + 1)
    max_length[0] = float('-inf')

    for i in range(n):
        j = bisect_right(max_length, A[i])
        if max_length[j - 1] <= A[i] < max_length[j]:
            max_length[j] = A[i]

    return len([v for v in max_length if float('-inf') < v < float('inf')])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "16-12-longest_nondecreasing_subsequence.py",
            'longest_nondecreasing_subsequence.tsv',
            longest_nondecreasing_subsequence_length))
