# https://leetcode.com/problems/flip-string-to-monotone-increasing/


class Solution(object):
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        count_end_with_ones, count_end_with_zeros = 0, 0
        for c in S:
            count_end_with_ones = min(count_end_with_ones, count_end_with_zeros)
            if c == '0':
                count_end_with_ones += 1
            else:
                count_end_with_zeros += 1

        return min(count_end_with_ones, count_end_with_zeros)
