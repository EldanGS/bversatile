# https://www.geeksforgeeks.org/auto-complete-feature-using-trie/
import collections


class TrieNode:
    def __init__(self):
        self.child = collections.defaultdict(TrieNode)
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            node = node.child[c]

        node.is_word = True


class Solution:
    def findWords(self, board, words) -> []:
        trie = Trie()
        result, node = [], trie.root

        # build Trie
        for word in words:
            trie.insert(word)

        for i in range(len(board)):
            for j in range(len(board[0])):
                self._search_word(board, i, j, node, '', result)

        return result

    def _search_word(self, board, i, j, node, path, result):
        if node.is_word:
            result.append(path)
            node.is_word = False

        if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] == '#':
            return

        temp = board[i][j]
        node = node.child.get(temp)
        if not node:
            return

        board[i][j] = '#'
        self._search_word(board, i + 1, j, node, path + temp, result)
        self._search_word(board, i - 1, j, node, path + temp, result)
        self._search_word(board, i, j + 1, node, path + temp, result)
        self._search_word(board, i, j - 1, node, path + temp, result)
        board[i][j] = temp
