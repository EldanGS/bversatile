# https://leetcode.com/problems/rearrange-string-k-distance-apart/

"""
Given a non-empty string s and an integer k,
rearrange the string such that the same characters are at least distance k from each other.

All input strings are given in lowercase letters.
If it is not possible to rearrange the string, return an empty string "".

Example 1:

Input: s = "aabbcc", k = 3
Output: "abcabc"
Explanation: The same letters are at least distance 3 from each other.
Example 2:

Input: s = "aaabc", k = 3
Output: ""
Explanation: It is not possible to rearrange the string.
Example 3:

Input: s = "aaadbbcc", k = 2
Output: "abacabcd"
Explanation: The same letters are at least distance 2 from each other.

"""

import heapq
import collections


class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if not k:
            return s

        max_heap = [(-freq, char)
                    for char, freq in collections.Counter(s).items()]
        heapq.heapify(max_heap)

        result = []
        while len(result) < len(s):
            if not max_heap:
                return ""
            cur_freq, cur_char = heapq.heappop(max_heap)
            stack = []
            result.append(cur_char)

            for _ in range(1, k):
                if len(result) == len(s):
                    return "".join(result)
                if not max_heap:
                    return ""

                next_freq, next_char = heapq.heappop(max_heap)
                result.append(next_char)

                if next_freq < -1:
                    stack.append((next_freq + 1, next_char))

            while stack:
                heapq.heappush(max_heap, stack.pop())
            heapq.heappush(max_heap, (cur_freq + 1, cur_char))

        return "".join(result)
