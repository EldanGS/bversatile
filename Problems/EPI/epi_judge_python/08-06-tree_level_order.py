from test_framework import generic_test


def binary_tree_depth_order(tree):
    depth_order = []
    if tree is None:
        return depth_order

    queue = [tree]
    while queue:
        depth_order.append([node.data for node in queue])
        queue = [node for curr in queue for node in [curr.left, curr.right] if node]

    return depth_order


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("08-06-tree_level_order.py",
                                       "tree_level_order.tsv",
                                       binary_tree_depth_order))
