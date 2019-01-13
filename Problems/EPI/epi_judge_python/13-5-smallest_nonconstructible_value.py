from test_framework import generic_test


def smallest_nonconstructible_value(A):
    max_constructible_value = 0
    for a in sorted(A):
        if a > max_constructible_value + 1:
            break
        max_constructible_value += a

    return max_constructible_value + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("13-5-smallest_nonconstructible_value.py",
                                       'smallest_nonconstructible_value.tsv',
                                       smallest_nonconstructible_value))
