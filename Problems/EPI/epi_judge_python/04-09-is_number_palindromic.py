from test_framework import generic_test
import math


def is_palindrome_number(x):
    if x <= 0:
        return x == 0

    rem_x, reverse_x = x, 0
    while rem_x:
        reverse_x = reverse_x * 10 + rem_x % 10
        rem_x //= 10

    return reverse_x == x


def is_palindrome_number2(x):
    if x <= 0:
        return x == 0

    num_of_digits = int(math.log10(x)) + 1
    mask = 10**(num_of_digits - 1)
    for _ in range(num_of_digits // 2):
        if x // mask != x % 10:
            return False
        x %= mask
        x //= 10
        mask //= 100

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("04-09-is_number_palindromic.py",
                                       "is_number_palindromic.tsv",
                                       is_palindrome_number))
