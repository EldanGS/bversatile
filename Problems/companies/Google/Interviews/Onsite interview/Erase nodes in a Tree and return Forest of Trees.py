"""
https://leetcode.com/discuss/interview-question/285350/Google-interview-question-Erase-nodes-in-a-Tree-and-return-Forest-of-Trees


You are given a binary tree and a function shouldBeErased(node to check whether a node should be erased). Erase all nodes that should be erased in the binary tree and return the resulting forest in the form of an array of every root node.

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
        result.append(root.val)

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


