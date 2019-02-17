# https://leetcode.com/problems/word-break/

import collections


class Solution:
    # O(N^2) time, O(N) space
    def wordBreak(self, s: 'str', wordDict: 'List[str]') -> 'bool':
        if not s or not wordDict:
            return False

        entity_words, visited = set(wordDict), set()
        q = collections.deque([0])

        while q:
            start = q.popleft()

            if start == len(s):
                return True

            if start not in visited:
                visited.add(start)

                for end in range(start, len(s)):
                    word = s[start:end + 1]
                    if word in entity_words:
                        q.append(end + 1)

        return False

    # O(N * M) time, O(N) space; More concise DP approach
    def wordBreak2(self, s: 'str', wordDict: 'List[str]') -> 'bool':
        dp = [False] * len(s)

        for i in range(len(s)):
            for w in wordDict:
                if w == s[i - len(w) + 1:i + 1] and (dp[i - len(w)] or i - len(w) == -1):
                    dp[i] = True
                    break
        return dp[-1]
