# https://leetcode.com/problems/kth-largest-element-in-an-array/

import heapq


class Solution:
    def findKthLargest(self, nums: 'List[int]', k: 'int') -> 'int':
        min_heap = []
        for num in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
            else:
                heapq.heappushpop(min_heap, num)

        return min_heap[0]

    """
    The basic idea is to use Quick Select algorithm to partition the array with pivot:

    Put numbers < pivot to pivot's left
    Put numbers > pivot to pivot's right
    Then
    
    if indexOfPivot == k, return A[k]
    else if indexOfPivot < k, keep checking left part to pivot
    else if indexOfPivot > k, keep checking right part to pivot
    Time complexity = O(n)
    
    Discard half each time: n+(n/2)+(n/4)..1 = n + (n-1) = O(2n-1) = O(n), because n/2+n/4+n/8+..1=n-1.
    """

    # O(N) time, O(1) space
    def findKthLargest2(self, nums, k):
        if not nums:
            raise IndexError('Array is empty')

        def quick_select(start, end, k):
            if start > end:
                return float('inf')

            pivot, left = nums[end], start
            for right in range(start, end):
                if nums[right] <= pivot:
                    nums[right], nums[left] = nums[left], nums[right]
                    left += 1

            nums[left], nums[end] = nums[end], nums[left]

            if left == k:
                return nums[left]
            elif left < k:
                return quick_select(left + 1, end, k)
            else:
                return quick_select(start, left - 1, k)

        return quick_select(0, len(nums) - 1, len(nums) - k)
