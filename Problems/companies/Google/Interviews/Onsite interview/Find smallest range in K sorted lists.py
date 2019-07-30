"""
https://www.careercup.com/question?id=16759664

You have k lists of sorted integers. Find the smallest range that includes at least one number from each of the k lists.

For example,
List 1: [4, 10, 15, 24, 26]
List 2: [0, 9, 12, 20]
List 3: [5, 18, 22, 30]

The smallest range here would be [20, 24] as it contains 24 from list 1, 20 from list 2, and 22 from list 3.


"""

import heapq


def smallest_range_in_K_lists(sequences):
    min_heap = []
    num_elements = 0
    for i, numbers in enumerate(sequences):
        min_heap.append((numbers[0], i, 0))
        num_elements += len(numbers)

    heapq.heapify(min_heap)
    left_bound, right_bound = min(min_heap)[0], max(min_heap)[0]
    for _ in range(num_elements):
        cur_left, cur_right = min(min_heap)[0], max(min_heap)[0]
        current_range = cur_right - cur_left

        if right_bound - left_bound > current_range:
            right_bound, left_bound = cur_right, cur_left

        _, i, j = heapq.heappop(min_heap)

        if j + 1 >= len(sequences[i]):
            break

        heapq.heappush(min_heap, (sequences[i][j + 1], i, j + 1))

    return [left_bound, right_bound]


if __name__ == '__main__':
    sequences = [[4, 10, 15, 24, 26],
               [0, 9, 12, 20],
               [5, 18, 22, 30]]

    print(smallest_range_in_K_lists(sequences))

