# https://www.geeksforgeeks.org/find-m-th-smallest-value-in-k-sorted-arrays/

"""

Given k sorted arrays of possibly different sizes, find m-th smallest value in the merged array.

Examples:

Input: m = 5
      arr[][] = { {1, 3},
                  {2, 4, 6},
                  {0, 9, 10, 11}} ;
Output: 4
Explanation The merged array would
be {0 1 2 3 4 6 9 10 11}.  The 5-th
smallest element in this merged
array is 4.

Input: M = 2
      arr[][] = { {1, 3, 20},
                  {2, 4, 6}} ;
Output: 2

Input: M = 6
      arr[][] = { {1, 3, 20},
                  {2, 4, 6}} ;
Output: 20

"""

import heapq


def m_smallest(lists, M) -> int:
    if not lists:
        return -1

    min_heap = []

    for i, l in enumerate(lists):
        if l:
            heapq.heappush(min_heap, (l[0], i, 1))

    candidate = -1
    while min_heap and M > 0:
        min_val, i, j = heapq.heappop(min_heap)

        if j < len(lists[i]):
            heapq.heappush(min_heap, (lists[i][j], i, j + 1))

        candidate, M = min_val, M - 1

    return candidate


def _test(lists, M, expected):
    actual = m_smallest(lists, M)

    assert actual == expected, 'Wrong answer, expected: {}, actual: {}'.format(expected, actual)
    print('Accepted')


if __name__ == '__main__':
    lists, M = [[1, 3], [2, 4, 6], [0, 9, 10, 11]], 5
    _test(lists, M, 4)

    lists, M = [[1, 3, 20], [2, 4, 6]], 2
    _test(lists, M, 2)

    lists, M = [[1, 3, 20], [2, 4, 6]], 6
    _test(lists, M, 20)
