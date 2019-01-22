import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def rotate_array(rotate_amount, A):
    def partition_rotation(begin, end):
        while begin < end:
            A[begin], A[end] = A[end], A[begin]
            begin, end = begin + 1, end - 1

    n = len(A)
    rotate_amount %= n
    if rotate_amount == 0:
        return

    partition_rotation(0, n - 1)
    partition_rotation(0, rotate_amount - 1)
    partition_rotation(rotate_amount, n - 1)


@enable_executor_hook
def rotate_array_wrapper(executor, A, rotate_amount):
    a_copy = A[:]
    executor.run(functools.partial(rotate_array, rotate_amount, a_copy))
    return a_copy


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("24-06-rotate_array.py", 'rotate_array.tsv',
                                       rotate_array_wrapper))
