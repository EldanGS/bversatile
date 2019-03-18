import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class BinaryTreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def reconstruct_preorder(preorder):
    def directed_reconstruct_preorder(preorder_iter):
        subtree_key = next(preorder_iter)
        if subtree_key is None:
            return None
        left_subtree = directed_reconstruct_preorder(preorder_iter)
        right_subtree = directed_reconstruct_preorder(preorder_iter)
        return BinaryTreeNode(subtree_key, left_subtree, right_subtree)

    return directed_reconstruct_preorder(iter(preorder))


@enable_executor_hook
def reconstruct_preorder_wrapper(executor, data):
    data = [None if x == 'null' else int(x) for x in data]
    return executor.run(functools.partial(reconstruct_preorder, data))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("09-13-tree_from_preorder_with_null.py",
                                       'tree_from_preorder_with_null.tsv',
                                       reconstruct_preorder_wrapper))
