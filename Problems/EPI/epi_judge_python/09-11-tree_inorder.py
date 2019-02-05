from test_framework import generic_test


def inorder_traversal(tree):
    prev, result = None, []
    while tree:
        if prev is tree.parent:
            if tree.left:
                next = tree.left
            else:
                result.append(tree.data)
                next = tree.right or tree.parent
        elif tree.left is prev:
            result.append(tree.data)
            next = tree.right or tree.parent
        else:
            next = tree.parent
        prev, tree = tree, next

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("09-11-tree_inorder.py", 'tree_inorder.tsv',
                                       inorder_traversal))
