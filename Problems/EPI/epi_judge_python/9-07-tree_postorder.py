from test_framework import generic_test


# We use stack and previous node pointer to simulate postorder traversal.
def postorder_traversal(tree):
    stack, result = [], []
    while True:
        while tree:
            stack.append(tree)
            stack.append(tree)
            tree = tree.left
        if not stack:
            break
        tree = stack.pop()
        if stack and stack[-1] == tree:
            tree = tree.right
        else:
            result.append(tree.data)
            tree = None

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "9-07-tree_postorder.py", 'tree_postorder.tsv', postorder_traversal))
