from test_framework import generic_test
from math import isclose


def square_root(x):
    left, right = (1.0, x) if x >= 1 else (x, 1.0)
    while not isclose(left, right):
        mid = (left + right) * 0.5
        if mid * mid > x:
            right = mid
        else:
            left = mid
    return left


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("11-05-real_square_root.py",
                                       'real_square_root.tsv', square_root))
