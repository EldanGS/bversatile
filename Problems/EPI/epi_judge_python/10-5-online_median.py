from test_framework import generic_test
import heapq


def online_median(sequence):
    min_heap, max_heap = [], []
    result = []
    for value in sequence:
        heapq.heappush(min_heap, -heapq.heappushpop(max_heap, value))
        if len(max_heap) < len(min_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))

        result.append(max_heap[0] if len(max_heap) > len(min_heap) else
                      (max_heap[0] - min_heap[0]) / 2)

    return result


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("10-5-online_median.py", "online_median.tsv",
                                       online_median_wrapper))
