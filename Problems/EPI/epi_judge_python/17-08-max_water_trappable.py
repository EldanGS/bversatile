from test_framework import generic_test


def calculate_trapping_water(heights):
    return 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("17-08-max_water_trappable.py",
                                       'max_water_trappable.tsv',
                                       calculate_trapping_water))
