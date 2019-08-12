# https://leetcode.com/problems/diagonal-traverse/submissions/

"""
Given a matrix of M x N elements (M rows, N columns),
return all elements of the matrix in diagonal order as shown in the below image.



Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]


"""


class Solution:
    def findDiagonalOrder(self, matrix) -> list:
        if not matrix or not matrix[0]:
            return []

        dirs = ((-1, 1), (1, -1))
        n, m = len(matrix), len(matrix[0])
        row = col = d = 0
        diagonal_order = []

        for _ in range(n * m):
            diagonal_order.append(matrix[row][col])
            row += dirs[d][0]
            col += dirs[d][1]

            if row >= n:
                row, col = n - 1, col + 2
                d ^= 1
            if col >= m:
                col, row = m - 1, row + 2
                d ^= 1

            if row < 0:
                row, d = 0, d ^ 1
            if col < 0:
                col, d = 0, d ^ 1

        return diagonal_order
