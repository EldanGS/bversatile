"""
Given a matrix of size n x m, the elements in the matrix are 0、1、2. 0 for the sea, 1 for the island, and 2 for the city
on the island(You can assume that 2 is built on 1, ie 2 also represents the island).
If two 1 are adjacent, then these two 1 belong to the same island.
Find the number of islands with at least one city.

    Notice
We only consider up, down, left and right as adjacent.
n <= 100，m <= 100.
You can assume that the four sides of the matrix are surrounded by the sea.

Example
Given mat =[
[1,1,0,0,0],
[0,1,0,0,1],
[0,0,0,1,1],
[0,0,0,0,0],
[0,0,0,0,1]]

return 0.
Explanation:There are 3 islands, but none of them contain cities.

Given mat =[
[1,1,0,0,0],
[0,1,0,0,1],
[0,0,2,1,2],
[0,0,0,0,0],
[0,0,0,0,2]]

return 2.
Explanation:There are 3 islands, and two of them have cities.

"""


def island_city(grid):
    if not grid or not grid[0]:
        return 0

    n, m = len(grid), len(grid[0])
    visited = [[False] * m for _ in range(n)]
    count = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2 and not visited[i][j]:
                dfs(i, j, grid, visited)
                count += 1

    return count


def dfs(i, j, grid, visited):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid):
        return

    if not grid[i][j] or visited[i][j]:
        return

    visited[i][j] = True
    grid[i][j] = 2
    dfs(i - 1, j, grid, visited)
    dfs(i + 1, j, grid, visited)
    dfs(i, j - 1, grid, visited)
    dfs(i, j + 1, grid, visited)


if __name__ == '__main__':
    grid = [[1, 1, 0, 0, 0],
            [0, 1, 0, 0, 1],
            [0, 0, 0, 1, 1],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1]]

    print(island_city(grid))

    grid = [[1, 1, 0, 0, 0],
            [0, 1, 0, 0, 1],
            [0, 0, 2, 1, 2],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 2]]

    print(island_city(grid))
