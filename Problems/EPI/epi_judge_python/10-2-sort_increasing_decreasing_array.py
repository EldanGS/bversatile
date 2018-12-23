from test_framework import generic_test
import heapq


def merge_sorted_subarrays(sorted_arrays):
    return list(heapq.merge(*sorted_arrays))


def sort_k_increasing_decreasing_array(A):
    sorted_subarrays = []
    sorted_type, start_idx = 0, 0  # sorted_type: 0 - increase, 1 - decrease
    for i in range(1, len(A) + 1):
        if (i == len(A) or
                (A[i - 1] < A[i] and sorted_type) or
                (A[i - 1] >= A[i] and not sorted_type)):
            sorted_subarrays.append(A[i - 1: start_idx - 1: -1] if sorted_type else
                                    A[start_idx:i])
            start_idx = i
            sorted_type ^= 1

    return merge_sorted_subarrays(sorted_subarrays)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("10-2-sort_increasing_decreasing_array.py",
                                       'sort_increasing_decreasing_array.tsv',
                                       sort_k_increasing_decreasing_array))
