"""
Given matrix, each row sorted by ascending order and each element in a row divided their position by row.
Try to find K largest elements in given matrix.

[
[x_1, x_2, ..., x_n]
[x_1 / 2, x_2 / 2, ..., x_n / 2]
[x_1 / 3, x_2 / 3, ..., x_n / 3]
[x_1 / 4, x_2 / 4, ..., x_n / 4]
...
]
"""
import heapq


def k_largest_in_matrix(matrix, k):
    if not matrix or not matrix[0]:
        return []

    k_largest, max_heap = [], []
    n, m = len(matrix), len(matrix[0])
    heapq.heappush(max_heap, (-matrix[0][-1], 0, m - 1))

    while len(k_largest) != k:
        val, i, j = heapq.heappop(max_heap)

        if i + 1 < n:
            heapq.heappush(max_heap, (-matrix[i + 1][j], i + 1, j))
        if j - 1 >= 0:
            heapq.heappush(max_heap, (-matrix[i][j - 1], i, j - 1))

        k_largest.append(-val)

    return k_largest


def test(matrix, k, expected):
    actual = k_largest_in_matrix(matrix, k)

    assert actual == expected, 'Incorrect answer, actual:{}'.format(actual)
    print('correct')


if __name__ == '__main__':
    matrix = [[1, 5,    11,   14,   20],
              [0, 2.5,  5.5,  7,    10],
              [0, 1.67, 3.67, 4.67, 6.67],
              [0, 1.25, 2.75, 3.5,  5.0],
              [0, 1.0,  2.2,  2.8,  4.0]]
    K = 5
    expected = [20, 14, 11, 10, 7]
    test(matrix, K, expected)
