from test_framework import generic_test


def find_nearest_repetition(paragraph):
    nearest_word = {}
    result = float('inf')
    for i, word in enumerate(paragraph):
        if word in nearest_word:
            result = min(result, i - nearest_word[word])

        nearest_word[word] = i

    return result if result != float('inf') else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("12-05-nearest_repeated_entries.py",
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
