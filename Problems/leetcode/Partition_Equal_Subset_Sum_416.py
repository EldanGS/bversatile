"""
Given a non-empty array containing only positive integers, find if the array
can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:

Each of the array element will not exceed 100.
The array size will not exceed 200.


Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].


Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.


"""

import functools


class Solution1:

    def canPartition(self, nums: list) -> bool:
        total = sum(nums)
        if total & 1:
            return False

        total >>= 1
        nums.sort()

        @functools.lru_cache(None)
        def dfs(target, index):
            if index == 0 or target <= 0:
                return target == 0

            return dfs(target - nums[index - 1], index - 1) or dfs(target,
                                                                   index - 1)

        return dfs(total, len(nums))


class Solution2:
    def canPartition(self, nums: list) -> bool:
        total = sum(nums)
        if total & 1:
            return False

        total >>= 1
        exist_sums = [True] + [False] * total

        for num in nums:
            for current_sum in range(total, 0, -1):
                if current_sum >= num:
                    exist_sums[current_sum] |= exist_sums[current_sum - num]

        return exist_sums[-1]


class Solution:

    def canPartition(self, nums: list) -> bool:
        total = sum(nums)
        if total & 1:
            return False

        total >>= 1
        entity_sums = {0}
        for num in nums:
            entity_sums.update({v + num for v in entity_sums})
            if total in entity_sums:
                return True

        return False
