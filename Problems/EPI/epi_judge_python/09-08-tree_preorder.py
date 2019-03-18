from test_framework import generic_test


def preorder_traversal(tree):
    if not tree:
        return []

    stack, result = [tree], []
    while stack:
        node = stack.pop()
        if node:
            result.append(node.data)
            stack += [node.right, node.left]

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("09-08-tree_preorder.py", 'tree_preorder.tsv',
                                       preorder_traversal))
