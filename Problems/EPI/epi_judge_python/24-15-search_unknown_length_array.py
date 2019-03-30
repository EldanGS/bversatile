from test_framework import generic_test


def binary_search_unknown_length(A, k):
    p = 0
    while True:
        try:
            idx = (1 << p) - 1
            if A[idx] == k:
                return idx
            elif A[idx] > k:
                break
        except IndexError:
            break
        p += 1

    left, right = 1 << max(0, (p - 1)), (1 << p) - 2
    while left <= right:
        mid = left + (right - left) // 2
        try:
            if A[mid] == k:
                return mid
            elif A[mid] > k:
                right = mid - 1
            else:
                left = mid + 1
        except IndexError:
            right = mid - 1

    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("24-15-search_unknown_length_array.py",
                                       'search_unknown_length_array.tsv',
                                       binary_search_unknown_length))
