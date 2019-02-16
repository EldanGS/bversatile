# https://leetcode.com/problems/minimum-window-substring/
import collections


class Solution:
    def minWindow(self, s: 'str', t: 'str') -> 'str':
        if not s or not t or len(t) > len(s):
            return ''

        entity_count = collections.Counter(t)
        target_length = len(t)
        substr_left, substr_right, left = 0, 0, 0

        for right, c in enumerate(s, 1):
            target_length -= 1 if entity_count[c] > 0 else 0
            entity_count[c] -= 1

            if not target_length:
                while left < right and entity_count[s[left]] < 0:
                    entity_count[s[left]] += 1
                    left += 1

                if not substr_right or substr_right - substr_left >= right - left:
                    substr_left, substr_right = left, right

        return s[substr_left: substr_right]