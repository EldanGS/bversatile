from test_framework import generic_test
import heapq


# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k, A):
    pass


# O(NlogK) time, O(K) space
def find_kth_largest(k, A):
    max_heap = []
    for a in A:
        if len(max_heap) < k:
            heapq.heappush(max_heap, a)
        else:
            val = heapq.heappop(max_heap)
            heapq.heappush(max_heap, max(val, a))

    return max_heap[0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("11-08-kth_largest_in_array.py",
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
