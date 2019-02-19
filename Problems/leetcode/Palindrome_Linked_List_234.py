# https://leetcode.com/problems/palindrome-linked-list/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverse_list(self, head):
        reversed_head = None
        while head:
            head.next, reversed_head, head = (reversed_head, head, head.next)

        return reversed_head

    def isPalindrome(self, head: 'ListNode') -> 'bool':
        if not head:
            return True

        slow = fast = head
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next

        reversed_tail = self.reverse_list(slow)
        while head:
            if reversed_tail.val != head.val:
                return False

            reversed_tail, head = reversed_tail.next, head.next

        return True
