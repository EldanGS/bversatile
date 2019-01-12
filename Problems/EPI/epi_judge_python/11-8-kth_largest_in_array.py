from test_framework import generic_test
import heapq, random, operator


# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest1(k, A):
    # TODO - you fill in here.
    max_heap = []
    for a in A:
        heapq.heappush(max_heap, a)
        if len(max_heap) > k:
            heapq.heappop(max_heap)

    return max_heap[0]


def find_kth_largest(k, A):
    def find_kth(comp):
        def partition_around_pivot(left, right, pivot_idx):
            pivot_value = A[pivot_idx]
            new_pivot_idx = left
            A[pivot_idx], A[right] = A[right], A[pivot_idx]
            for i in range(left, rssight):
                if comp(A[i], pivot_value):
                    A[i], A[new_pivot_idx] = A[new_pivot_idx], A[i]
                    new_pivot_idx += 1
            A[right], A[new_pivot_idx] = A[new_pivot_idx], A[right]
            return new_pivot_idx

        left, right = 0, len(A) - 1
        while left <= right:
            pivot_idx = random.randint(left, right)
            new_pivot_idx = partition_around_pivot(left, right, pivot_idx)
            if new_pivot_idx == k - 1:
                return A[new_pivot_idx]
            elif new_pivot_idx > k - 1:
                right = new_pivot_idx - 1
            else:
                left = new_pivot_idx + 1

    return find_kth(operator.gt)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("11-8-kth_largest_in_array.py",
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
