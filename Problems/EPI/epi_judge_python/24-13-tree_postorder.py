from test_framework import generic_test


# We use stack and previous node pointer to simulate postorder traversal.
def postorder_traversal2(tree):
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


def postorder_traversal(tree):
    if not tree:
        return []

    path_stack, prev, postorder_sequence = [tree], None, []
    while path_stack:
        curr = path_stack[-1]
        if not prev or prev.left is curr or prev.right is curr:
            if curr.left:
                path_stack.append(curr.left)
            elif curr.right:
                path_stack.append(curr.right)
            else:
                postorder_sequence.append(curr.data)
                path_stack.pop()
        elif curr.left is prev:
            if curr.right:
                path_stack.append(curr.right)
            else:
                postorder_sequence.append(curr.data)
                path_stack.pop()
        else:
            postorder_sequence.append(curr.data)
            path_stack.pop()
        prev = curr

    return postorder_sequence


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "24-13-tree_postorder.py", 'tree_postorder.tsv', postorder_traversal))
