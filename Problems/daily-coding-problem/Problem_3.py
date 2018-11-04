"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class Tree:
    def __init__(self):
        self.root = None

    def addNode(self, node, value):
        if node == None:
            self.root = Node(value)
        else:
            if value < node.value:
                if not node.left:
                    node.left = Node(value)
                else:
                    self.addNode(node.left, value)
            else:
                if not node.right:
                    node.right = Node(value)
                else:
                    self.addNode(node.right, value)

def serialize(root):
	values = []
	def serializer(node):
		if not node:
			values.append('null')
		else:
			values.append(str(node.value))
			serializer(node.left)
			serializer(node.right)
	serializer(root)

	return ','.join(values)

def deserialize(s):
    values = iter(s.split(','))
    def deserializer():
        val = next(values)
        if val == 'null':
            return None
        else:
            node = Node(int(val))
            node.left = deserializer()
            node.right = deserializer()
            return node
    
    return deserializer()


if __name__ == '__main__':
    # Read input, numbers separated by commas
    numbers = [int(n) for n in input().split(',')]
    theTree = Tree()
    for number in numbers:
        theTree.addNode(theTree.root, number)
    s1 = serialize(theTree.root)
    s2 = serialize(deserialize(s1))
    print(s1) 
    print(s2)
    assert s1 == s2
