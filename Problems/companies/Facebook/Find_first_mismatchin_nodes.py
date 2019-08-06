"""
Return first pair of mismatching nodes (first pair as in in-order) given two pre-order traversal arrays of BSTs.

Example 1:

Input: pre1 = [5, 4, 2, 4, 8, 6, 9], pre2 = [5, 3, 2, 4, 8, 7, 9]
Output: [4, 3]
Explanation:
Tree 1:
	 5
  4     8
2  4   6  9

Tree 2:
	 5
  3     8
2  4   7  9

inorder1 = [2, 4, 4, 5, 6, 8, 9]
inorder2 = [2, 3, 4, 5, 7, 8, 9]

Example 2:

Input: pre1 = [2, 1, 3], pre2 = [1, 2]
Output: [3, null]
Explanation:
Tree 1:
  2
1   3

Tree 2:
	1
	   2

inorder1 = [1, 2, 3]
inorder2 = [1, 2]


Example 3:

Input: pre1 = [2, 1, 3], pre2 = [1, 2, 3]
Output: []
Explanation:
Tree 1:
	2
  1   3

Tree 2:
	1
	   2
		  3

inorder1 = [1, 2, 3]
inorder2 = [1, 2, 3]

There is no mismatch because the in-order sequence for both is exactly the SAME,
despite the trees are structurally different.

"""


class TreeNode:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_mismatch(root1, root2):
    stack1, stack2 = [], []
    result = []

    while stack1 or root1:
        while root1 or root2:
            if root1:
                stack1.append(root1)
                root1 = root1.left
            if root2:
                stack2.append(root2)
                root2 = root2.left

        root1 = stack1.pop() if stack1 else None
        root2 = stack2.pop() if stack2 else None

        if root1 and root2 and root1.val != root2.val:
            result += [root1.val, root2.val]
        elif root1 and not root2:
            result += [root1.val, None]
        elif root2 and not root1:
            result += [root2.val, None]

        root1 = root1.right if root1 else None
        root2 = root2.right if root2 else None

    return result


if __name__ == '__main__':
    """
    Input: pre1 = [2, 1, 3], pre2 = [1, 2, 3]
    Output: []
    Explanation:
    Tree 1:
        2
      1   3
    
    Tree 2:
        1
           2
              3
    
    inorder1 = [1, 2, 3]
    inorder2 = [1, 2, 3]
    """
    root1 = TreeNode(2)
    root1_left = TreeNode(1)
    root1_right = TreeNode(3)

    root1.left = root1_left
    root1.right = root1_right

    root2 = TreeNode(1)
    root2_right = TreeNode(2)
    root2_right_right = TreeNode(3)

    root2.right = root2_right
    root2_right.right = root2_right_right

    print(find_mismatch(root1, root2))

    """
    Example 2:
    Input: pre1 = [2, 1, 3], pre2 = [1, 2]
    Output: [3, null]
    Explanation:
    Tree 1:
      2
    1   3
    
    Tree 2:
        1
           2
    
    inorder1 = [1, 2, 3]
    inorder2 = [1, 2]
    """

    root1 = TreeNode(2)
    root1_left = TreeNode(1)
    root1_right = TreeNode(3)

    root1.left = root1_left
    root1.right = root1_right

    root2 = TreeNode(1)
    root2_right = TreeNode(2)
    root2.right = root2_right

    print(find_mismatch(root1, root2))
