"""
Given an N * NN∗N matrix where each row and column is sorted in ascending order,
ind the Kth smallest element in the matrix.

Example 1:
Input: Matrix=[
    [2, 6, 8],
    [3, 7, 10],
    [5, 8, 11]
  ],
  K=5
Output: 7
Explanation: The 5th smallest number in the matrix is 7.

"""

from heapq import *


def find_Kth_smallest(matrix, k):
    number = -1
    min_heap = []
    for i, row in enumerate(matrix):
        min_heap.append((row[0], i, 1))

    heapify(min_heap)
    while k > 0 and min_heap:
        number, i, j = heappop(min_heap)
        k -= 1
        if j < len(matrix[i]):
            heappush(min_heap, (matrix[i][j], i, j + 1))

    return number if k == 0 else -1


def find_Kth_smallest_bin_search(matrix, k):
    left, right = matrix[0][0], matrix[-1][-1]
    while left < right:
        mid = left + (right - left) // 2
        smaller, larger = matrix[0][0], matrix[-1][-1]
        count, smaller, larger = count_less_equal(matrix, mid, smaller, larger)

        if count == k:
            return mid
        if count < k:
            left = larger
        else:
            right = smaller
    return left


def count_less_equal(matrix, mid, smaller, larger):
    count, n = 0, len(matrix)
    row, col = n - 1, 0
    while row >= 0 and col < n:
        if matrix[row][col] > mid:
            # as matrix[row][col] is bigger than the mid, let's keep track of the
            # smallest number greater than the mid
            larger = min(larger, matrix[row][col])
            row -= 1
        else:
            # as matrix[row][col] is less than or equal to the mid, let's keep track of the
            # biggest number less than or equal to the mid
            smaller = max(smaller, matrix[row][col])
            count += row + 1
            col += 1

    return count, smaller, larger


def main():
    print("Kth smallest number is: " +
          str(find_Kth_smallest([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5)))

    print("Kth smallest number is: " +
          str(find_Kth_smallest_bin_search([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5)))

main()
