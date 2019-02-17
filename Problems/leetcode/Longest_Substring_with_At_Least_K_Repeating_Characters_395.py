# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/

import collections


# O(N * 26) time, O(N) by pace
class Solution:
    def longestSubstring(self, s: 'str', k: 'int') -> 'int':
        def longest_substring_with_h_unique_chars(s, k, h):
            entity_count = collections.Counter()
            longest_substr, unique_chars, no_less_than_k = 0, 0, 0
            start, end = 0, 0

            while end < len(s):
                entity_count[s[end]] += 1

                if entity_count[s[end]] == 1:
                    unique_chars += 1
                if entity_count[s[end]] == k:
                    no_less_than_k += 1
                end += 1

                while unique_chars > h:
                    entity_count[s[start]] -= 1

                    if entity_count[s[start]] == 0:
                        unique_chars -= 1
                    if entity_count[s[start]] == k - 1:
                        no_less_than_k -= 1
                    start += 1

                if unique_chars == no_less_than_k:
                    longest_substr = max(longest_substr, end - start)

            return longest_substr

        return max(longest_substring_with_h_unique_chars(s, k, i) for i in range(1, 27))
