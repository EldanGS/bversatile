# https://leetcode.com/problems/binary-search-tree-iterator/


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator(object):

    def __init__(self, root):
        self.nodes = []
        self._push_nodes(root)

    def next(self):
        node = self.nodes.pop()
        self._push_nodes(node.right)

        return node.val

    def hasNext(self):
        return len(self.nodes) > 0

    def _push_nodes(self, node):
        while node is not None:
            self.nodes.append(node)
            node = node.left

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
