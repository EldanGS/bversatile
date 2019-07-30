"""
You are given a m x n 2D grid initialized with these three possible values.

1) -1 <-> A wall or an obstacle.
2) 0 <-> A gate.
3) INF <-> Infinity means an empty room. We use the value 2^31 - 1 = 2147483647 to represent INF as you may assume
that the distance to a gate is less than 2147483647.

Fill each empty room with the distance to its nearest gate.
If it is impossible to reach a gate, it should be filled with INF.

For example, given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF

After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4

"""
from collections import deque


def wall_and_gates(grid):
    if not grid or not grid[0]:
        return grid

    GATE, EMPTY = 0, 2 ** 31 - 1
    n, m = len(grid), len(grid[0])
    queue = deque([])

    for i in range(n):
        for j in range(m):
            if grid[i][j] == GATE:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()

        for next_x, next_y in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= next_x < n and 0 <= next_y < m and grid[next_x][next_y] == EMPTY:
                grid[next_x][next_y] = grid[x][y] + 1
                queue.append((next_x, next_y))

    return grid


if __name__ == '__main__':
    INF = 2 ** 31 - 1
    grid = [[INF, -1, 0, INF], [INF, INF, INF, -1], [INF, -1, INF, -1], [0, -1, INF, INF]]

    for row in grid:
        print(row)

    print('\n')

    for row in wall_and_gates(grid):
        print(row)
