# Definition for singly-linked list.
import heapq


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return []

        min_heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i))

        dummy_head = temp = ListNode(None)
        while min_heap:
            min_value, current_index_of_list = heapq.heappop(min_heap)

            if lists[current_index_of_list]:
                temp.next = lists[current_index_of_list]
                temp = temp.next

            if lists[current_index_of_list].next:
                heapq.heappush(min_heap, (lists[current_index_of_list].next.val, current_index_of_list))
                lists[current_index_of_list] = lists[current_index_of_list].next

        return dummy_head.next
