from test_framework import generic_test


# We use stack and previous node pointer to simulate postorder traversal.
def postorder_traversal(tree):
    if not tree:
        return []

    stack, result = [], []
    while True:
        while tree:
            if tree.right:
                stack.append(tree.right)

            stack.append(tree)
            tree = tree.left

        tree = stack.pop()

        if tree.right and stack and stack[-1] is tree.right:
            stack.pop()
            stack.append(tree)
            tree = tree.right
        else:
            result.append(tree.data)
            tree = None

        if not stack:
            break

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "tree_postorder.py", 'tree_postorder.tsv', postorder_traversal))
