# https://leetcode.com/problems/longest-consecutive-sequence/


class Solution:
    def longestConsecutive(self, nums: 'List[int]') -> 'int':
        longest_sequence = 0
        entity_nums = set(nums)

        for num in nums:
            if num - 1 not in entity_nums:
                current_num = num + 1
                while current_num in entity_nums:
                    current_num += 1

                longest_sequence = max(longest_sequence, current_num - num)

        return longest_sequence
