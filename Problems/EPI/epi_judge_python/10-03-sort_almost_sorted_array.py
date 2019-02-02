from test_framework import generic_test
import itertools
import heapq


def sort_approximately_sorted_array(sequence, k):
    min_heap = []
    for x in itertools.islice(sequence, k):
        heapq.heappush(min_heap, x)

    result = []
    for x in sequence:
        smallest = heapq.heappushpop(min_heap, x)
        result.append(smallest)

    while min_heap:
        smallest = heapq.heappop(min_heap)
        result.append(smallest)

    return result


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "10-03-sort_almost_sorted_array.py", 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
