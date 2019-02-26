# https://leetcode.com/problems/custom-sort-string/

import collections, string


class Solution:
    def customSortString(self, S: str, T: str) -> str:
        if not S or not T:
            return ''

        counter_T = collections.Counter(T)
        result = ''
        for c in S:
            while counter_T[c] > 0:
                result += c
                counter_T[c] -= 1

        for c in string.ascii_lowercase:
            while counter_T[c] > 0:
                result += c
                counter_T[c] -= 1

        return result

