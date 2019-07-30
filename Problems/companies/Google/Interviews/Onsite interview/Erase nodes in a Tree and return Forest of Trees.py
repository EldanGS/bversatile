"""
https://leetcode.com/discuss/interview-question/285350/Google-interview-question-Erase-nodes-in-a-Tree-and-return-Forest-of-Trees


You are given a binary tree and a function shouldBeErased(node to check whether a node should be erased).
Erase all nodes that should be erased in the binary tree and return the resulting forest in the form of an array of every root node.

	               A
				/      \
			 [B]        C
		   /      \         \
	     P          Q         R
		/    \
	E       [ M]

	Assume Nodes B and M can be deleted in a Tree


	The result is a list of TreeNodes [A,        P,        Q]
	                                  /   \     /
									  null C   E
											 \
											  R


"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def erase_nodes(root, erased):
    result = []
    if not root:
        return result

    erase_nodes_helper(root, erased, result)

    if root not in erased:
        result.append(root)

    return result


def erase_nodes_helper(node, erased, result):
    if not node:
        return None

    node.left = erase_nodes_helper(node.left, erased, result)
    node.right = erase_nodes_helper(node.right, erased, result)

    if node.val in erased:
        if node.left:
            result.append(node.left)
        if node.right:
            result.append(node.right)

        return None

    return node


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.right = Node(5)
    root.left.right = Node(6)

    erased = {2, 5}

    result = erase_nodes(root, erased)
    for node in result:
        print(node.val)
    """
            1
        [2]      3
     4      6       [5]
        
    """
