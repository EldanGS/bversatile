from test_framework import generic_test


def has_two_sum(A, t):
    left, right = 0, len(A) - 1

    while left <= right:
        if A[left] + A[right] > t:
            right -= 1
        elif A[left] + A[right] < t:
            left += 1
        else:
            return True

    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("two_sum.py", 'two_sum.tsv',
                                       has_two_sum))
