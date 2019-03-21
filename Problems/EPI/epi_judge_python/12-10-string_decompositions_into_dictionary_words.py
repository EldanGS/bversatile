from test_framework import generic_test
from collections import Counter


def find_all_substrings(s, words):
    if not s or not words:
        return []

    def match_all_words_in_dict(start):
        current_string_to_freq = Counter()

        for i in range(start, start + len(words) * unit_size, unit_size):
            current_word = s[i:i + unit_size]
            original_freq = words_freq[current_word]
            if original_freq == 0:
                return False

            current_string_to_freq[current_word] += 1

            if current_string_to_freq[current_word] > original_freq:
                return False

        return True

    words_freq = Counter(words)
    unit_size = len(words[0])

    return [i for i in range(len(s) - unit_size * len(words) + 1)
            if match_all_words_in_dict(i)]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "12-10-string_decompositions_into_dictionary_words.py",
            'string_decompositions_into_dictionary_words.tsv',
            find_all_substrings))
