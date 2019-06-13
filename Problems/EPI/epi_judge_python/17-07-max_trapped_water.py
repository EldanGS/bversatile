from test_framework import generic_test


def get_max_trapped_water(heights):
    left, right = 0, len(heights) - 1
    max_trapped_water = 0

    while left < right:
        width = right - left
        max_trapped_water = max(max_trapped_water, min(heights[left], heights[right]) * width)

        if heights[left] > heights[right]:
            right -= 1
        else:
            left += 1

    return max_trapped_water


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("17-07-max_trapped_water.py",
                                       "max_trapped_water.tsv",
                                       get_max_trapped_water))
