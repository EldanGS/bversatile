# https://leetcode.com/problems/word-search/


class Solution:
    def exist(self, board: 'List[List[str]]', word: 'str') -> 'bool':
        def word_search(x, y, word_index):
            if word_index == len(word):
                return True

            if not (0 <= x < len(board) and 0 <= y < len(board[x])) or board[x][y] != word[word_index] or board[x][
                y] == '#':
                return False

            c = board[x][y]
            board[x][y] = '#'  # fill visited chars
            for next_x, next_y in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if word_search(next_x, next_y, word_index + 1):
                    return True

            board[x][y] = c
            return False

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0] and word_search(i, j, 0):
                    return True

        return False
