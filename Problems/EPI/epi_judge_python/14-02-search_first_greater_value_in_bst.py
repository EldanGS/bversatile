from test_framework import generic_test


def find_first_greater_than_k(tree, k):
    greatest_so_far = None
    while tree:
        if tree.data > k:
            greatest_so_far, tree = tree, tree.left
        else:
            tree = tree.right

    return greatest_so_far


def find_first_greater_than_k_wrapper(tree, k):
    result = find_first_greater_than_k(tree, k)
    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("14-02-search_first_greater_value_in_bst.py",
                                       'search_first_greater_value_in_bst.tsv',
                                       find_first_greater_than_k_wrapper))
