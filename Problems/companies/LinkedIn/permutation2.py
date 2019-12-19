"""
https://leetcode.com/problems/permutations-ii/

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

"""
import collections


class Solution:
    def permutation_helper(self, perm, n, counter, result):
        if len(perm) == n:
            result.append(perm[:])
            return

        for x in counter:
            if counter[x] > 0:
                counter[x] -= 1
                perm.append(x)
                self.permutation_helper(perm, n, counter, result)
                counter[x] += 1
                perm.pop()

    def permuteUnique(self, nums: list) -> list:
        counter = collections.Counter(nums)
        result = []

        self.permutation_helper([], len(nums), counter, result)
        return result
