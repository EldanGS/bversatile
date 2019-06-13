import functools
import collections

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(tree, node0, node1):
    q = collections.deque([tree])
    parents = {tree: None}

    while node0 not in parents or node1 not in parents:
        node = q.popleft()
        if node.left:
            parents[node.left] = node
            q.append(node.left)
        if node.right:
            parents[node.right] = node
            q.append(node.right)

    path = set()
    while node0:
        path.add(node0)
        node0 = parents[node0]

    while node1 not in path:
        node1 = parents[node1]

    return node1


def lca(tree, node0, node1):
    Status = collections.namedtuple('Status', ('num_target_nodes', 'ancestor'))

    def lca_helper(tree, node0, node1):
        if not tree:
            return Status(0, None)

        left_subtree = lca_helper(tree.left, node0, node1)
        if left_subtree.num_target_nodes == 2:
            return left_subtree

        right_subtree = lca_helper(tree.right, node0, node1)
        if right_subtree.num_target_nodes == 2:
            return right_subtree

        num_target_nodes = (left_subtree.num_target_nodes +
                            right_subtree.num_target_nodes +
                            (node0, node1).count(tree))
        return Status(num_target_nodes, tree if num_target_nodes == 2 else None)

    return lca_helper(tree, node0, node1).ancestor


# O(H) time, O(N) space
def lca(tree, node0, node1):
    q = collections.deque([tree])
    parents = {tree: None}

    while node0 not in parents or node1 not in parents:
        node = q.popleft()
        if node.left:
            parents[node.left] = node
            q.append(node.left)

        if node.right:
            parents[node.right] = node
            q.append(node.right)

    path = set()
    while node0:
        path.add(node0)
        node0 = parents[node0]

    while node1 not in path:
        node1 = parents[node1]

    return node1


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
        generic_test.generic_test_main("09-03-lowest_common_ancestor.py",
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
