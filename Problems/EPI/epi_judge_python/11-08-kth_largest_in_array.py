from test_framework import generic_test
import heapq


# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.

# O(N) time, O(1) space
def find_kth_largest(k, A):
    if not A:
        raise IndexError('Array is empty')

    return quick_select(A, 0, len(A) - 1, len(A) - k)


def quick_select(A, start, end, k):
    if start > end:
        return float('inf')

    pivot, left = A[end], start  # Take A[end] as the pivot
    for i in range(start, end):
        if A[i] <= pivot:  # Put numbers < pivot to pivot's left
            A[i], A[left] = A[left], A[i]
            left += 1

    A[left], A[end] = A[end], A[left]  # Finally, swap A[end] with A[left]

    if left == k:  # Found kth smallest number
        return A[left]
    if left < k:  # Check right part
        return quick_select(A, left + 1, end, k)
    else:
        return quick_select(A, start, left - 1, k)


# O(NlogK) time, O(K) space
def find_kth_largest2(k, A):
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
