from test_framework import generic_test
import collections


# Solution DFS
def is_binary_tree_bst1(tree, low_range=float('-inf'), high_range=float('inf')):
    if not tree:
        return True
    elif not low_range <= tree.data <= high_range:
        return False
    return is_binary_tree_bst(tree.left, low_range, tree.data) \
           and is_binary_tree_bst(tree.right, tree.data, high_range)


# Solution BFS
def is_binary_tree_bst(tree, low_range=float('-inf'), high_range=float('inf')):
    QueueEntry = collections.namedtuple('QueueEntry', ('node', 'lower', 'upper'))
    queue = collections.deque([QueueEntry(tree, low_range, high_range)])

    while queue:
        front = queue.popleft()
        if front.node:
            if not front.lower <= front.node.data <= front.upper:
                return False
            queue += [
                QueueEntry(front.node.left, front.lower, front.node.data),
                QueueEntry(front.node.right, front.node.data, front.upper)
            ]

    return True

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("14-01-is_tree_a_bst.py", 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
