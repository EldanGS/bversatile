from test_framework import generic_test


def calculate_trapping_water(heights):
    left, right = 0, len(heights) - 1
    max_water_trapped = 0
    left_max, right_max = 0, 0

    while left < right:
        if heights[left] <= heights[right]:
            if left_max <= heights[left]:
                left_max = heights[left]
            else:
                max_water_trapped += left_max - heights[left]
            left += 1
        else:
            if right_max <= heights[right]:
                right_max = heights[right]
            else:
                max_water_trapped += right_max - heights[right]
            right -= 1

    return max_water_trapped


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("17-00-max_water_trappable.py",
                                       'max_water_trappable.tsv',
                                       calculate_trapping_water))
