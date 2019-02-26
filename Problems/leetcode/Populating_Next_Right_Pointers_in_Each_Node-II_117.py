# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/


# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        def merge_level(node):
            while node:
                head, tail = None, None
                while node:
                    if node.left:
                        if not tail:
                            head = node.left
                        else:
                            tail.next = node.left
                        tail = node.left
                    if node.right:
                        if not tail:
                            head = node.right
                        else:
                            tail.next = node.right
                        tail = node.right
                    node = node.next
                node = head

        merge_level(root)
        return root
