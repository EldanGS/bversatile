"""
https://leetcode.com/problems/word-ladder-ii/

Given two words (beginWord and endWord), and a dictionary's word list,
find all shortest transformation sequence(s) from beginWord to endWord,
such that:

Only one letter can be changed at a time Each transformed word must exist in
the word list. Note that beginWord is not a transformed word. Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible
transformation.
"""

import collections
import string


class Solution:
    def findLadders(self, begin_word: str, end_word: str,
                    word_list: List[str]) -> List[List[str]]:
        word_list = set(word_list)
        if end_word not in word_list:
            return []

        result = []
        layer = {begin_word: [[begin_word]]}

        while layer:
            new_layer = collections.defaultdict(list)
            for word in layer:
                if word == end_word:
                    result.extend(l for l in layer[word])
                else:
                    for i in range(len(word)):
                        for c in string.ascii_lowercase:
                            cur = word[:i] + c + word[i + 1:]
                            if cur in word_list:
                                new_layer[cur] += [temp + [cur] for temp in
                                                   layer[word]]

            word_list ^= set(new_layer.keys())
            layer = new_layer

        return result
