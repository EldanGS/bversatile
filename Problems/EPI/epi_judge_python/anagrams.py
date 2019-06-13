from test_framework import generic_test, test_utils
from collections import defaultdict


def find_anagrams(dictionary):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23,
              29, 31, 37, 41, 43, 47, 53, 59,
              61, 67, 71, 73, 79, 83, 89, 97,
              101, 103]

    anagrams_map = defaultdict(list)
    for word in dictionary:
        word_hash = 1
        for c in word:
            if 'a' <= c <= 'z':
                word_hash *= primes[ord(c) - 97]

        if word_hash in anagrams_map:
            anagrams_map[word_hash].append(word)
        else:
            anagrams_map[word_hash] = [word]

    return [group for group in anagrams_map.values() if len(group) >= 2]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "anagrams.py",
            "anagrams.tsv",
            find_anagrams,
            comparator=test_utils.unordered_compare))
