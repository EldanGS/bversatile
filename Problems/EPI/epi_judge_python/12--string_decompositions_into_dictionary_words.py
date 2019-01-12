from test_framework import generic_test
import collections


def find_all_substrings(s, words):
    data_words = collections.Counter(words)
    block = len(words[0])

    def match_all_words_in_dict(start):
        curr_string_to_freq = collections.Counter()
        for i in range(start, start + len(words) * block, block):
            curr_word = s[i:i + block]
            it = data_words[curr_word]
            if it == 0:
                return False

            curr_string_to_freq[curr_word] += 1
            if curr_string_to_freq[curr_word] > it:
                return False
        return True

    return [i for i in range(len(s) - block * len(words) + 1)
            if match_all_words_in_dict(i)] + [0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "12--string_decompositions_into_dictionary_words.py",
            'string_decompositions_into_dictionary_words.tsv',
            find_all_substrings))
