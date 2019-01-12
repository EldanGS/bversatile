from test_framework import generic_test


class BstNode:
    def __init__(self, data, left, right):
        self.data, self.left, self.right = data, left, right


def rebuild_bst_from_preorder(preorder_sequence):
    def rebuild_bst_from_preorder_on_value_range(lower_bound, upper_bound):
        if root_idx[0] == len(preorder_sequence):
            return None

        root = preorder_sequence[root_idx[0]]
        if not lower_bound <= root <= upper_bound:
            return None

        root_idx[0] += 1
        left_subtree = rebuild_bst_from_preorder_on_value_range(lower_bound, root)
        right_subtree = rebuild_bst_from_preorder_on_value_range(root, upper_bound)

        return BstNode(root, left_subtree, right_subtree)

    root_idx = [0]
    return rebuild_bst_from_preorder_on_value_range(float('-inf'), float('inf'))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("14-05-bst_from_preorder.py",
                                       'bst_from_preorder.tsv',
                                       rebuild_bst_from_preorder))
