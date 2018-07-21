# https://leetcode.com/problems/reverse-linked-list/description/

"""
Solution.
Complexity analysis:
Time: O(N) - always
Memory: O(N) - in worst case
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while head != None:
            next = head.next
            head.next = prev
            prev = head
            head = next
        
        return prev
