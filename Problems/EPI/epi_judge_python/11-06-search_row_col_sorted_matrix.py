from test_framework import generic_test


# O(NlogM) time, O(1) space
def matrix_search2(A, x):
    for row in A:
        left, right = 0, len(row) - 1
        while left <= right:
            mid = (left + right) // 2
            if row[mid] == x:
                return True
            elif row[mid] > x:
                right = mid - 1
            else:
                left = mid + 1

    return False


# O(N + M) time, O(1) space
def matrix_search(A, x):
    row, col = 0, len(A[0]) - 1
    while row < len(A) and col >= 0:
        if A[row][col] == x:
            return True
        elif A[row][col] < x:
            row += 1
        else:
            col -= 1

    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("11-06-search_row_col_sorted_matrix.py",
                                       'search_row_col_sorted_matrix.tsv',
                                       matrix_search))
