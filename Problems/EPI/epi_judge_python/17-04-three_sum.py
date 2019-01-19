from test_framework import generic_test


def has_two_sum(A, t):
    left, right = 0, len(A) - 1
    while left <= right:
        current_sum = A[left] + A[right]
        if current_sum > t:
            right -= 1
        elif current_sum < t:
            left += 1
        else:
            return True

    return False


def has_three_sum(A, t):
    A.sort()
    return any(has_two_sum(A, t - a) for a in A)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("17-04-three_sum.py", "three_sum.tsv",
                                       has_three_sum))
