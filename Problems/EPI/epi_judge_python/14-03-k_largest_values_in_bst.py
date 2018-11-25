from test_framework import generic_test, test_utils


def find_k_largest_in_bst(tree, k):
    def helper(tree):
        if tree and len(k_largest_elements) < k:
            helper(tree.right)
            if len(k_largest_elements) < k:
                k_largest_elements.append(tree.data)
                helper(tree.left)

    k_largest_elements = []
    helper(tree)

    return k_largest_elements


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "14-03-k_largest_values_in_bst.py", 'k_largest_values_in_bst.tsv',
            find_k_largest_in_bst, test_utils.unordered_compare))
