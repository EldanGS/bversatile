from test_framework import generic_test
import collections


def is_letter_constructible_from_magazine1(letter_text, magazine_text):
    char_frequency_for_letter = collections.Counter(magazine_text)
    for c in letter_text:
        if not char_frequency_for_letter.get(c, False):
            return False
        char_frequency_for_letter[c] -= 1

    return True


def is_letter_constructible_from_magazine(letter_text, magazine_text):
    return not (collections.Counter(letter_text) - collections.Counter(magazine_text))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("12-02-is_anonymous_letter_constructible.py",
                                       'is_anonymous_letter_constructible.tsv',
                                       is_letter_constructible_from_magazine))
