from test_framework import generic_test
from heapq import *


def merge_sorted_arrays(sorted_arrays):
    min_heap = []
    for A in sorted_arrays:
        for value in A:
            heappush(min_heap, value)

    result = []
    while min_heap:
        result.append(heappop(min_heap))

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("10-1-sorted_arrays_merge.py",
                                       "sorted_arrays_merge.tsv",
                                       merge_sorted_arrays))
