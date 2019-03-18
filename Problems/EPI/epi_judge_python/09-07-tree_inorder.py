from test_framework import generic_test


def inorder_traversal(tree):
    if not tree:
        return []

    stack, result = [], []
    while stack or tree:
        if tree:
            stack.append(tree)
            tree = tree.left
        else:
            tree = stack.pop()
            result.append(tree.data)
            tree = tree.right

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("09-07-tree_inorder.py", 'tree_inorder.tsv',
                                       inorder_traversal))
