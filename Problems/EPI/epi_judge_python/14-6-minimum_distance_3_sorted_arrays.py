from test_framework import generic_test
import bintrees


# O(NlogK) time, O(logK) space
def find_closest_elements_in_sorted_arrays(sorted_arrays):
    tree = bintrees.RBTree()
    for array_idx, sorted_array in enumerate(sorted_arrays):
        it = iter(sorted_array)
        first_min = next(it, None)
        if first_min is not None:
            tree.insert((first_min, array_idx), it)

    min_distance_so_far = float('inf')
    while True:
        current_min, current_min_idx = tree.min_key()
        current_max = tree.max_key()[0]
        min_distance_so_far = min(min_distance_so_far, current_max - current_min)

        next_it = tree.pop_min()[1]
        next_min = next(next_it, None)
        if next_min is None:
            break

        tree.insert((next_min, current_min_idx), next_it)

    return min_distance_so_far


if __name__ == '__main__':
    # sorted_arrays = [[5, 10, 15], [3, 6, 9, 12, 15], [8, 16, 24]]
    # print(find_closest_elements_in_sorted_arrays(sorted_arrays))

    exit(
        generic_test.generic_test_main("14-6-minimum_distance_3_sorted_arrays.py",
                                       'minimum_distance_3_sorted_arrays.tsv',
                                       find_closest_elements_in_sorted_arrays))
