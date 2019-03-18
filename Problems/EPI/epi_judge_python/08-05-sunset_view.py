from test_framework import generic_test
import collections


def examine_buildings_with_sunset(sequence):
    BuildingWithHeight = collections.namedtuple('BuildingWithHeight', ('id', 'height'))
    candidates = []
    for building_id, height in enumerate(sequence):
        while candidates and candidates[-1].height <= height:
            candidates.pop()
        candidates.append(BuildingWithHeight(building_id, height))

    return [candidate.id for candidate in reversed(candidates)]


def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("08-05-sunset_view.py", 'sunset_view.tsv',
                                       examine_buildings_with_sunset))
