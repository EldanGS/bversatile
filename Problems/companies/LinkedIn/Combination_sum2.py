"""
https://leetcode.com/problems/combination-sum-ii/

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]


"""


class Solution:
    def combination_generator(self, start, path, nums, target, result):
        if target < 0:
            return

        if target == 0:
            result.append(path)
            return

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue

            if nums[i] > target:
                break

            self.combination_generator(i + 1, path + [nums[i]], nums,
                                       target - nums[i], result)

    def combinationSum2(self, candidates: list, target: int) -> list:
        result = []
        self.combination_generator(0, [], sorted(candidates), target, result)
        return result
