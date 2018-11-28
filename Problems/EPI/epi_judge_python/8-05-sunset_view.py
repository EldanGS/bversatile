from test_framework import generic_test
import collections


def examine_buildings_with_sunset(sequence):
    building_with_height = collections.namedtuple('building_with_height', ('id', 'height'))
    candidates = []
    for index, height in enumerate(sequence):
        while candidates and height >= candidates[-1].height:
            candidates.pop()
        candidates.append(building_with_height(index, height))

    return [c.id for c in reversed(candidates)]


def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("8-05-sunset_view.py", 'sunset_view.tsv',
                                       examine_buildings_with_sunset))
