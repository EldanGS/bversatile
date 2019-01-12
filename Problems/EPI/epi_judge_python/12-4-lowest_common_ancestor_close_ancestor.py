import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(node0, node1):
    iter0, iter1 = node0, node1
    data_nodes = set()
    while iter0 or iter1:
        if iter0:
            if iter0 in data_nodes:
                return iter0
            data_nodes.add(iter0)
            iter0 = iter0.parent
        if iter1:
            if iter1 in data_nodes:
                return iter1
            data_nodes.add(iter1)
            iter1 = iter1.parent
    return ValueError('node0 and node are not in the same tree')


@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "12-4-lowest_common_ancestor_close_ancestor.py",
            'lowest_common_ancestor.tsv', lca_wrapper))
