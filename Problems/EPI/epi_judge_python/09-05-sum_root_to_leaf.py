from test_framework import generic_test


def sum_root_to_leaf(tree, partial_path_sum=0) -> int:
    if not tree:
        return 0

    partial_path_sum = (partial_path_sum << 1) | tree.data
    if not tree.left and not tree.right:
        return partial_path_sum

    return sum_root_to_leaf(tree.left, partial_path_sum) + sum_root_to_leaf(tree.right, partial_path_sum)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "09-05-sum_root_to_leaf.py", 'sum_root_to_leaf.tsv', sum_root_to_leaf))
