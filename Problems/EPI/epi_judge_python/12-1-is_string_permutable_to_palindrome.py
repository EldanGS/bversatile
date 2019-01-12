from test_framework import generic_test
import collections


# Solution #1: O(N) time, O(C) space; where N is length of s, C is unique characters
def can_form_palindrome1(s):
    data = {}
    for c in s:
        data[c] = data.get(c, 0) + 1
    odd = 0
    for k, v in data.items():
        if v & 1:
            odd += 1
    return not odd > 1


# Solution #2: O(N) time, O(C) space; where N is length of s, C is unique characters
def can_form_palindrome(s):
    return sum(v % 2 for v in collections.Counter(s).values()) <= 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "12-1-is_string_permutable_to_palindrome.py",
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
