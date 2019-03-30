from test_framework import generic_test
import heapq


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


def find_kth_largest_unknown_length(stream, k):
    candidates = []
    for x in stream:
        candidates.append(x)
        if len(candidates) >= 2 * k - 1:
            find_kth_largest(k, candidates)
            del candidates[k:]

    find_kth_largest(k, candidates)

    return candidates[k - 1]


# Pythonic solution that uses library method but costs O(nlogk) time.
def find_kth_largest_unknown_length_pythonic(stream, k):
    return heapq.nlargest(k, stream)[-1]


def find_kth_largest_unknown_length_wrapper(stream, k):
    return find_kth_largest_unknown_length(iter(stream), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "24-17-kth_largest_element_in_long_array.py",
            'kth_largest_element_in_long_array.tsv',
            find_kth_largest_unknown_length_wrapper))
