from test_framework import generic_test
import itertools


def find_maximum_subarray(A):
    if not A:
        return -1
    min_sum = max_sum = A[0]
    for running_sum in itertools.accumulate(A[1:]):
        min_sum = min(min_sum, running_sum)
        max_sum = max(max_sum, running_sum - min_sum)

    return max_sum


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("max_sum_subarray.py",
                                       'max_sum_subarray.tsv',
                                       find_maximum_subarray))
