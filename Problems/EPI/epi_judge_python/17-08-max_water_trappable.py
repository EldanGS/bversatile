from test_framework import generic_test


def calculate_trapping_water(heights):
    pillar_indices, max_rectangle_area = [], 0

    for i, h in enumerate(heights + [0]):
        while pillar_indices and heights[pillar_indices[-1]] >= h:
            height = heights[pillar_indices.pop()]
            width = i - pillar_indices[-1] - 1 if pillar_indices else i
            max_rectangle_area = max(max_rectangle_area, height * width)
        pillar_indices.append(i)

    return max_rectangle_area


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("17-08-max_water_trappable.py",
                                       'max_water_trappable.tsv',
                                       calculate_trapping_water))
