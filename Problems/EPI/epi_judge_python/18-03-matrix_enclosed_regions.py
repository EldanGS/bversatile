from test_framework import generic_test
from collections import deque


def fill_surrounded_regions(board):
    n, m = len(board), len(board[0])
    queue = deque([(i, j) for k in range(n) for i, j in ((k, 0), (k, m - 1))] +
                  [(i, j) for k in range(m) for i, j in ((0, k), (n - 1, k))])

    while queue:
        x, y = queue.popleft()
        if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == 'W':
            board[x][y] = '#'
            queue.extend([(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)])

    board[:] = [['B' if c != '#' else 'W' for c in row] for row in board]


def fill_surrounded_regions_wrapper(board):
    fill_surrounded_regions(board)
    return board


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("18-03-matrix_enclosed_regions.py",
                                       'matrix_enclosed_regions.tsv',
                                       fill_surrounded_regions_wrapper))
