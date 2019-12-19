"""
https://leetcode.com/problems/longest-consecutive-sequence/

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

"""


class Solution:
    def __init__(self):
        self.parent = {}

    def find(self, x, nums):
        if x in self.parent and self.parent[x] != x - 1:
            return self.parent[x]
        if x - 1 in nums:
            self.parent[x] = self.find(x - 1, nums)
            return self.parent[x]
        return x - 1

    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        result = 0
        for num in nums:
            result = max(result, num - self.find(num, nums))

        return result
