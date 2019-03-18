from test_framework import generic_test, test_utils
from heapq import *


# O(NlogK) time, O(K) space
def k_largest_in_binary_heap2(A, k):
    assert len(A) >= k, 'A length is less than K'

    max_heap = []
    for a in A:
        if len(max_heap) < k:
            heapq.heappush(max_heap, a)
        else:
            if max_heap[0] < a:
                heapq.heappushpop(max_heap, a)

    return max_heap


# O(KlogK) time, O(K) space
def k_largest_in_binary_heap(A, k):
    assert len(A) >= k, 'A length is less than K'
    candidate_max_heap, result = [], []
    heappush(candidate_max_heap, (-A[0], 0))

    for _ in range(k):
        candidate, candidate_idx = heappop(candidate_max_heap)
        result.append(-candidate)

        left_child_idx = 2 * candidate_idx + 1
        if left_child_idx < len(A):
            heappush(candidate_max_heap, (-A[left_child_idx], left_child_idx))

        right_child_idx = 2 * candidate_idx + 2
        if right_child_idx < len(A):
            heappush(candidate_max_heap, (-A[right_child_idx], right_child_idx))

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "10-06-k_largest_in_heap.py",
            "k_largest_in_heap.tsv",
            k_largest_in_binary_heap,
            comparator=test_utils.unordered_compare))
