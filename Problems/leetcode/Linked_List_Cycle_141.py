# https://leetcode.com/problems/linked-list-cycle/description/


"""
1st solution.
Complexity analysis:
Time: O(N) - in worst case
Memory: O(N) - in worst case
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        data = dict()
        index = 0
        
        while head:
            if data.get(head) and data[head] < index:
                return True
            data[head] = index
            
            head = head.next
            index += 1
        
        return False


"""
2nd solution.
Complexity analysis:
Time: O(N) - in worst case
Memory: O(1) - always?
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            
            return True
        except:
            return False
                
        
