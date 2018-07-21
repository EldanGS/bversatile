# https://leetcode.com/problems/design-linked-list/description/

"""
Solution.
Complexity analysis:
Time: O(N) - ?
Memory: O(N) - in worst case
"""

class MyLinkedList:
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None

    def __init__(self):
        self.head = MyLinkedList.ListNode(0)
        self.size = 0

    def get(self, index):
        node = self.get_node(index + 1)
        return node.val if node else -1
    
    def get_node(self, index):
        if 0 <= index and index <= self.size:
            node = self.head
            while index:
                node = node.next
                index -= 1
            
            return node
        
        return None
                
    def addAtHead(self, val):
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index, val):
        if 0 <= index and index <= self.size:
            node = self.get_node(index)
            next_node = node.next
            node.next = MyLinkedList.ListNode(val)
            node.next.next = next_node
            self.size += 1
            
    def deleteAtIndex(self, index):
        if 0 <= index and index <= self.size:
            node = self.get_node(index)
            if node and node.next:
                node.next = node.next.next
                self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)