# https://leetcode.com/problems/kth-largest-element-in-an-array/

import heapq


class Solution(object):
    # O(NlogK) time, O(K) space
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_heap = []
        for num in nums:
            if len(max_heap) < k:
                heapq.heappush(max_heap, num)
            else:
                val = heapq.heappop(max_heap)
                heapq.heappush(max_heap, max(val, num))

        return max_heap[0]

    # O(N) time, O(1) space
    def findKthLargest2(self, nums, k):
        pass
