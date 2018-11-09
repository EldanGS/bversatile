from test_framework import generic_test
from test_framework.test_failure import TestFailure

import functools
import string

def int_to_string(x):
    sign = 0 if x >= 0 else 1
    result = []
    x = abs(x)

    while True:
        result.append(chr(ord('0') + x % 10))
        x //= 10
        if x == 0:
            break

    return ('-' if sign else '') + ''.join(reversed(result))

# def string_to_int(s):
#     sign = 1 if s[0] == '-' else 0
#     value = 0
#     for i in range(sign, len(s)):
#         value = value * 10 + int(s[i])
#
#     if sign:
#         value = -value
#
#     return value

def string_to_int(s):
    return functools.reduce(
        lambda runnig_sum, c: runnig_sum * 10 + string.digits.index(c),
        s[s[0] == '-':], 0) * (-1 if s[0] == '-' else 1)

def wrapper(x, s):
    if int_to_string(x) != s:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("6-01-string_integer_interconversion.py",
                                       'string_integer_interconversion.tsv',
                                       wrapper))
