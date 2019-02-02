from test_framework import generic_test, test_utils


def find_k_largest_in_bst(tree, k):
    k_largest = []

    def helper(tree):
        if tree and len(k_largest) < k:
            helper(tree.right)
            if len(k_largest) < k:
                k_largest.append(tree.data)
            helper(tree.left)

    helper(tree)
    return k_largest


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "14-03-k_largest_values_in_bst.py", 'k_largest_values_in_bst.tsv',
            find_k_largest_in_bst, test_utils.unordered_compare))
