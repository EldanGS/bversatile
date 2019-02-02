from test_framework import generic_test
from test_framework.test_failure import TestFailure
import string, functools


def int_to_string(x):
    sign = '-' if x < 0 else ''
    x = abs(x)

    s = []
    while True:
        s.append(chr(ord('0') + x % 10))
        x //= 10
        if x == 0:
            break

    return sign + ''.join(reversed(s))


def string_to_int(s):
    if not s:
        raise ValueError('Given string is empty')

    return functools.reduce(lambda running_sum, c:
                            running_sum * 10 + string.digits.index(c), s[s[0] == '-':], 0) * (-1 if s[0] == '-' else 1)


def wrapper(x, s):
    if int_to_string(x) != s:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("06-01-string_integer_interconversion.py",
                                       'string_integer_interconversion.tsv',
                                       wrapper))
