from test_framework import generic_test
from functools import reduce


def roman_to_integer(s):
    if not s:
        return 0

    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    return reduce(
        lambda num, i: num + (-roman[s[i]] if roman[s[i]] < roman[s[i + 1]] else roman[s[i]]),
        reversed(range(len(s) - 1)), roman[s[-1]])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "06-09-roman_to_integer.py", 'roman_to_integer.tsv', roman_to_integer))
