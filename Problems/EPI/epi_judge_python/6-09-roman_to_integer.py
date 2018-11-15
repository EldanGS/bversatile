from test_framework import generic_test

import functools


def roman_to_integer(s):
    data = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    return functools.reduce(
        lambda value, i: value + (-data[s[i]] if data[s[i]] < data[s[i + 1]] else data[s[i]]),
        reversed(range(len(s) - 1)), data[s[-1]]
    )


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "6-09-roman_to_integer.py", 'roman_to_integer.tsv', roman_to_integer))
