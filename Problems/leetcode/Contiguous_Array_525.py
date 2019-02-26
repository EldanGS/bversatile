# https://leetcode.com/problems/contiguous-array/


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_length, count = 0, 0
        table = {0: 0}

        for index, num in enumerate(nums, 1):
            if num:
                count += 1
            else:
                count -= 1

            if count in table:
                max_length = max(max_length, index - table[count])
            else:
                table[count] = index

        return max_length
