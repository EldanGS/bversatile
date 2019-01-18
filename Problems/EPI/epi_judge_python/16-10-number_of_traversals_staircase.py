from test_framework import generic_test


# My solution
def number_of_ways_to_top1(top, maximum_step):
    top += 1
    number_of_ways = [0] * top
    number_of_ways[0], number_of_ways[1] = 1, 1
    for i in range(2, top):
        j = 1
        while j <= maximum_step and j <= i:
            number_of_ways[i] = number_of_ways[i] + number_of_ways[i - j]
            j += 1

    return number_of_ways[-1]


# Author solution
def number_of_ways_to_top(top, maximum_step):
    def compute_number_of_ways_to_h(h):
        if h <= 1:
            return 1
        if number_of_ways[h] == 0:
            number_of_ways[h] = sum(compute_number_of_ways_to_h(h - i)
                                    for i in range(1, min(maximum_step, h) + 1))
        return number_of_ways[h]

    number_of_ways = [0] * (top + 1)
    return compute_number_of_ways_to_h(top)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("16-10-number_of_traversals_staircase.py",
                                       "number_of_traversals_staircase.tsv",
                                       number_of_ways_to_top))
