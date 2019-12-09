"""
https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/

Given a matrix, and a target, return the number of non-empty submatrices that sum to target.
A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.
Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.


Example 1:
Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
Output: 4
Explanation: The four 1x1 submatrices that only contain 0.
Example 2:

Input: matrix = [[1,-1],[-1,1]], target = 0
Output: 5
Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.

"""


# O(N*M^2) by time. N is rows, M is columns.
# O(N*M) by space if couldn't modify matrix else O(N).
def count_target_sum_in_matrix(matrix, target) -> int:
    n, m = len(matrix), len(matrix[0])
    for i in range(n):
        for j in range(1, m):
            matrix[i][j] += matrix[i][j - 1]

    result = 0
    for distance in range(m):
        for j in range(distance, m):
            prefix, current_sum = {0: 1}, 0
            for i in range(n):
                current_sum += matrix[i][j] - (matrix[i][distance - 1] if distance > 0 else 0)
                result += prefix.get(current_sum - target, 0)
                prefix[current_sum] = prefix.get(current_sum, 0) + 1
    return result


def test_count_target_sum_in_matrix(matrix, target, expected):
    actual = count_target_sum_in_matrix(matrix, target)

    assert actual == expected, 'Wrong answer: actual={}, expected={}'.format(actual, expected)
    print('Accepted')




