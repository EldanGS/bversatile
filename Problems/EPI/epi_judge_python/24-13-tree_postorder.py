from test_framework import generic_test


# We use stack and previous node pointer to simulate postorder traversal.
def postorder_traversal(tree):
    def inverted_preorder_traversal(tree):
        path_stack, result = [tree], []
        while path_stack:
            node = path_stack.pop()

            if not node:
                continue
            result.append(node.data)
            path_stack.extend([node.left, node.right])

        return result

    return inverted_preorder_traversal(tree)[::-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "24-13-tree_postorder.py", 'tree_postorder.tsv', postorder_traversal))
