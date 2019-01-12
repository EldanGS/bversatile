from test_framework import generic_test


# O(NlogN) time, O(N) space
def longest_contained_range(A):
    data = set(A)
    max_interval_size = 0
    while data:
        a = data.pop()
        lower_bound = a - 1
        while lower_bound in data:
            data.remove(lower_bound)
            lower_bound -= 1

        upper_bound = a + 1
        while upper_bound in data:
            data.remove(upper_bound)
            upper_bound += 1

        max_interval_size = max(max_interval_size, upper_bound - lower_bound - 1)

    return max_interval_size


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("12-9-longest_contained_interval.py",
                                       'longest_contained_interval.tsv',
                                       longest_contained_range))
