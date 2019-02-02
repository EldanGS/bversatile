from test_framework import generic_test
import collections


def can_form_palindrome(s):
    return sum(c & 1 for c in collections.Counter(s).values()) <= 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "12-01-is_string_permutable_to_palindrome.py",
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
