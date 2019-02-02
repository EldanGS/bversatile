from test_framework import generic_test


def merge_two_sorted_arrays(A, m, B, n):
    i, j = m - 1, n - 1
    write_index = n + m - 1
    while i >= 0 and j >= 0:
        if A[i] < B[j]:
            A[write_index] = B[j]
            j -= 1
        else:
            A[write_index] = A[i]
            i -= 1
        write_index -= 1

    while j >= 0:
        A[write_index] = B[j]
        write_index, j = write_index - 1, j - 1

    return A


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("13-02-two_sorted_arrays_merge.py",
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
