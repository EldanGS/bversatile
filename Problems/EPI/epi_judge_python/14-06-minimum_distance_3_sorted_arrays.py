from test_framework import generic_test
from bintrees import RBTree


def find_closest_elements_in_sorted_arrays(sorted_arrays):
    min_distance_so_far = float('inf')
    tree = RBTree()

    for idx, sorted_array in enumerate(sorted_arrays):
        array_iter = iter(sorted_array)
        first_min = next(array_iter, None)
        tree.insert((first_min, idx), array_iter)

    while True:
        min_value, min_index = tree.min_key()
        max_value = tree.max_key()[0]

        min_distance_so_far = min(min_distance_so_far, max_value - min_value)

        it = tree.pop_min()[1]
        next_min = next(it, None)

        if next_min is None:
            break

        tree.insert((next_min, min_index), it)

    return min_distance_so_far


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("14-06-minimum_distance_3_sorted_arrays.py",
                                       'minimum_distance_3_sorted_arrays.tsv',
                                       find_closest_elements_in_sorted_arrays))
