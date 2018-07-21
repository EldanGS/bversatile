# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

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
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        
        temp = head
        
        while temp.next:
            if temp.next.val == temp.val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        
        return head
