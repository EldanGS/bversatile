from test_framework import generic_test
import heapq


def merge_sorted_arrays(sorted_arrays):
    min_heap = []
    for i, array in enumerate(sorted_arrays):
        heapq.heappush(min_heap, (array[0], i, 0))

    result = []
    while min_heap:
        smallest_entry, smallest_array_i, j = heapq.heappop(min_heap)
        result.append(smallest_entry)

        if j + 1 < len(sorted_arrays[smallest_array_i]):
            heapq.heappush(min_heap, (sorted_arrays[smallest_array_i][j + 1], smallest_array_i, j + 1))

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("10-01-sorted_arrays_merge.py",
                                       "sorted_arrays_merge.tsv",
                                       merge_sorted_arrays))
