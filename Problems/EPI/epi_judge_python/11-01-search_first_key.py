from test_framework import generic_test


def search_first_of_k(A, k):
    left, right, result = 0, len(A) - 1, -1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] > k:
            right = mid - 1
        elif A[mid] == k:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "11-01-search_first_key.py", 'search_first_key.tsv', search_first_of_k))
