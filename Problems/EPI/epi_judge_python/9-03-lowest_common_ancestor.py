import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook
import collections


def lca(tree, node0, node1):
    Status = collections.namedtuple('Status', ('num_target_nodes', 'ancestor'))

    def lca_helper(tree, node0, node1):
        if not tree:
            return Status(0, None)

        left_subtree = lca_helper(tree.left, node0, node1)
        if left_subtree.num_target_nodes == 2:
            # Found both nodes in the left subtree
            return left_subtree

        right_subtree = lca_helper(tree.right, node0, node1)
        if right_subtree.num_target_nodes == 2:
            # Found both nodes in the right subtree
            return right_subtree

        num_target_nodes = (
                left_subtree.num_target_nodes + right_subtree.num_target_nodes +
                (node0, node1).count(tree))
        return Status(num_target_nodes, tree if num_target_nodes == 2 else None)

    return lca_helper(tree, node0, node1).ancestor


@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("9-03-lowest_common_ancestor.py",
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))