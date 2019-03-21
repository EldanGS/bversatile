from test_framework import generic_test


def number_of_ways_to_top(top, maximum_step):
    number_of_ways = [1] + [0] * top
    for h in range(1, top + 1):
        for step in range(1, maximum_step + 1):
            if h >= step:
                number_of_ways[h] += number_of_ways[h - step]

    return number_of_ways[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("16-10-number_of_traversals_staircase.py",
                                       "number_of_traversals_staircase.tsv",
                                       number_of_ways_to_top))
