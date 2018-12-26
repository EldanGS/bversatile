from test_framework import generic_test


# O(NlogM), where N is row, M is column
def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > x:
            right = mid - 1
        elif arr[mid] == x:
            return True
        else:
            left = mid + 1
    return False


def matrix_search2(A, x):
    for row in A:
        if binary_search(row, x):
            return True
    return False


# O(N + M) by time, O(1) by space
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
        generic_test.generic_test_main("11-6-search_row_col_sorted_matrix.py",
                                       'search_row_col_sorted_matrix.tsv',
                                       matrix_search))
