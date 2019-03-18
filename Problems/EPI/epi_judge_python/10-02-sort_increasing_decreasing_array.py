from test_framework import generic_test
import heapq

def merge_sorted_arrays(arrays):
    min_heap = []
    for array_index, array in enumerate(arrays):
        if array:
            heapq.heappush(min_heap, (array[0], array_index, 0))

    result = []
    while min_heap:
        smallest_entry, smallest_arr_idx, i = heapq.heappop(min_heap)
        result.append(smallest_entry)

        if i + 1 < len(arrays[smallest_arr_idx]):
            heapq.heappush(min_heap, (arrays[smallest_arr_idx][i + 1], smallest_arr_idx, i + 1))

    return result


def sort_k_increasing_decreasing_array(A):
    sorted_subarrays = []
    INCREASING, DECREASING = range(2)
    subarray_type = INCREASING
    left = 0

    for right in range(1, len(A) + 1):
        if (right == len(A) or
            (A[right - 1] < A[right] and subarray_type == DECREASING) or
            (A[right - 1] >= A[right] and subarray_type == INCREASING)):
            sorted_subarrays.append(A[left:right] if subarray_type == INCREASING else
                                    A[right - 1:left - 1:-1])
            left = right
            subarray_type = (DECREASING if subarray_type == INCREASING else INCREASING)

    return merge_sorted_arrays(sorted_subarrays)


if __name__ == '__main__':
    # A = [57, 131, 493, 294, 221, 339, 418, 452, 442, 190]
    # print(sort_k_increasing_decreasing_array(A))
    exit(
        generic_test.generic_test_main("10-02-sort_increasing_decreasing_array.py",
                                       'sort_increasing_decreasing_array.tsv',
                                       sort_k_increasing_decreasing_array))
