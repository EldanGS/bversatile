from test_framework import generic_test
import collections


def is_balanced_binary_tree(tree):
    BalancedStatusWithHeight = collections.namedtuple(
        'BalancedStatusWithHeight', ('balanced', 'height'))

    def check_balanced(tree):
        if not tree:
            return BalancedStatusWithHeight(True, -1)  # Base case

        left_result = check_balanced(tree.left)
        if not left_result.balanced:
            return BalancedStatusWithHeight(False, 0)

        right_result = check_balanced(tree.right)
        if not right_result.balanced:
            return BalancedStatusWithHeight(False, 0)

        is_balanced = abs(left_result.height - right_result.height) <= 1
        height = max(left_result.height, right_result.height) + 1
        return BalancedStatusWithHeight(is_balanced, height)

    return check_balanced(tree).balanced


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("9-01-is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
