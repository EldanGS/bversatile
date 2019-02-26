# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        convert = []

        def serializer(node):
            if not node:
                convert.append('null')
            else:
                convert.append(str(node.val))
                serializer(node.left)
                serializer(node.right)

        serializer(root)
        return ','.join(convert)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        reconvert = iter(data.split(','))

        def deserializer():
            value = next(reconvert)
            if value == 'null':
                return None
            else:
                node = TreeNode(int(value))
                node.left = deserializer()
                node.right = deserializer()
                return node

        return deserializer()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
