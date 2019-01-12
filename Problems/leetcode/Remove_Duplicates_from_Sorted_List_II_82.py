# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/

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
        
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        curr = head
        
        while curr:
            if curr.next and curr.val == curr.next.val:
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                
                prev.next = curr.next
            else:
                prev = prev.next
            
            curr = curr.next
        
        return dummy.next
        
                
                
        
