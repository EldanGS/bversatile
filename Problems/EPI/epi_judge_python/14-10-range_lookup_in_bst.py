import collections

from test_framework import generic_test

Interval = collections.namedtuple('Interval', ('left', 'right'))


def range_lookup_in_bst(tree, interval):
    def helper(tree):
        if tree is None:
            return None

        if interval.left <= tree.data <= interval.right:
            helper(tree.left)
            result.append(tree.data)
            helper(tree.right)
        elif interval.left > tree.data:
            helper(tree.right)
        else:
            helper(tree.left)

    result = []
    helper(tree)

    return result


def range_lookup_in_bst_wrapper(tree, i):
    return range_lookup_in_bst(tree, Interval(*i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("14-10-range_lookup_in_bst.py",
                                       'range_lookup_in_bst.tsv',
                                       range_lookup_in_bst_wrapper))
