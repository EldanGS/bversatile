from test_framework import generic_test
import collections


# Solution 1: O(N + M) time, O(C) space; where C is unique characters in M
def is_letter_constructible_from_magazine1(letter_text, magazine_text):
    if len(letter_text) > len(magazine_text):
        return False

    data_magazine = collections.Counter(magazine_text)
    for c in letter_text:
        if not data_magazine.get(c):
            return False
        data_magazine[c] -= 1

    return True


# Solution 2 pythonic: O(N + M) time, O(C) space
def is_letter_constructible_from_magazine(letter_text, magazine_text):
    return not collections.Counter(letter_text) - collections.Counter(magazine_text)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("12-2-is_anonymous_letter_constructible.py",
                                       'is_anonymous_letter_constructible.tsv',
                                       is_letter_constructible_from_magazine))
