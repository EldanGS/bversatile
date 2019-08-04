# https://leetcode.com/discuss/interview-question/301192/Facebook-or-Phone-screen-or-Shortest-Path-with-Obstacles

"""
Facebook Phone Interview Question.
I couldn't solve the problem of enumerating the path itself. Please share your working solution if you figure it out.

Given a 2D matrix where some of the elements are filled with 1 and the rest of the elements are filled with X, except 2
elements, of which one is S (start point) and E (endpoint). Here X means you cannot traverse to that particular point.
From a cell you can either traverse to left, right, up or down.
Given two points in the matrix find the shortest path between these points.
For example, if the matrix is
1 1 1 1 1
S 1 X 1 1
1 1 1 1 1
X 1 1 E 1
1 1 1 1 X

One of the shortest paths (from E to S both exclusive) is: [(3, 2), (3, 1), (2, 1), (2, 0)].
Return null if there is no path between S and E.

"""
import collections


def bfs(start_x, start_y, end_x, end_y, parent, matrix):
    queue = collections.deque((start_x, start_y))

    while queue:
        x, y = queue.popleft()

        if x == end_x and y == end_y:
            break

        for next_x, next_y in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if (0 <= next_x < len(matrix) and 0 <= next_y < len(matrix[0])
                    and matrix[next_x][next_y] == '1' and parent[next_x][next_y] == float('INF')):
                queue.append((next_x, next_y))
                parent[next_x][next_y] = parent[x][y] + 1


def short_path(matrix):
    if not matrix or not matrix[0]:
        return []

    n, m = len(matrix), len(matrix[0])
    start_x, start_y = -1, -1
    end_x, end_y = -1, -1

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 'S':
                start_x, start_y = i, j
            elif matrix[i][j] == 'E':
                end_x, end_y = i, j

    if start_x != -1 and end_x != -1:
        parent = [[float('inf')] * m for _ in range(n)]
        parent[start_x][start_y] = 0
        bfs(start_x, start_y, end_x, end_y, parent, matrix)

        path = []
        while parent[end_x][end_y] != 0:
            path.append((end_x, end_y))

            

    return []
