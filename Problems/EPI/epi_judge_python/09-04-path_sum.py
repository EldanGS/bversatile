from test_framework import generic_test


def has_path_sum(tree, remaining_weight):
    if not tree:
        return False
    if not tree.left and not tree.right:
        return remaining_weight == tree.data

    return (has_path_sum(tree.left, remaining_weight - tree.data) or
            has_path_sum(tree.right, remaining_weight - tree.data))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("09-04-path_sum.py", 'path_sum.tsv',
                                       has_path_sum))
