from test_framework import generic_test


def square_root(k):
    left, right = 0, k
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == k:
            return mid
        elif mid * mid > k:
            right = mid - 1
        else:
            left = mid + 1

    return right


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("11-04-int_square_root.py",
                                       "int_square_root.tsv", square_root))
