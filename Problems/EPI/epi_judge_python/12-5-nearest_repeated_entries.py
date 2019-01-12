from test_framework import generic_test


def find_nearest_repetition(paragraph):
    nearest_repeated_distance, data = float('inf'), {}
    for i, word in enumerate(paragraph):
        if word in data:
            nearest_repeated_distance = min(nearest_repeated_distance, i - data[word])
        data[word] = i

    return nearest_repeated_distance if nearest_repeated_distance != float('inf') \
        else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("12-5-nearest_repeated_entries.py",
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
