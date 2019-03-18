from test_framework import generic_test
from heapq import *


def online_median(sequence):
    result, min_heap, max_heap = [], [], []
    for num in sequence:
        heappush(max_heap, -heappushpop(min_heap, num))

        if len(max_heap) > len(min_heap):
            heappush(min_heap, -heappop(max_heap))

        result.append(0.5 * (min_heap[0] + (-max_heap[0]))
                      if len(min_heap) == len(max_heap) else min_heap[0])

    return result


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("10-05-online_median.py", "online_median.tsv",
                                       online_median_wrapper))
