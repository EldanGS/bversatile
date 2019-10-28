"""https://leetcode.com/problems/shortest-word-distance-ii/

Design a class which receives a list of words in the constructor, and implements
a method that takes two words word1 and word2 and return the shortest distance between
these two words in the list. Your method will be called repeatedly many times
with different parameters.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
"""
import collections


class WordDistance:

    def __init__(self, words):
        self.word_map = collections.defaultdict(list)
        for i, word in enumerate(words):
            self.word_map[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        list1, list2 = self.word_map[word1], self.word_map[word2]
        min_diff = float('inf')
        i, j = 0, 0
        while i < len(list1) and j < len(list2):
            min_diff = min(min_diff, abs(list1[i] - list2[j]))
            if list1[i] < list2[j]:
                i += 1
            else:
                j += 1

        return min_diff

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)
