# https://leetcode.com/problems/number-of-distinct-islands/description/


"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

Example 1:

11000
11000
00011
00011
Given the above grid map, return 1.
Example 2:

11011
10000
00001
11011
Given the above grid map, return 3.

Notice that:
11
1
and
 1
11
are considered different island shapes, because we do not consider reflection / rotation.
Note: The length of each dimension in the given grid does not exceed 50.
"""


class Solution:
    def numDistinctIslands(self, grid: 'List[List[int]]') -> 'int':
        def dfs(x, y, group, state):
            grid[x][y] = 0

            for direction in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                next_x, next_y = x + direction[0], y + direction[1]
                if 0 <= next_x < rows and 0 <= next_y < cols and grid[next_x][next_y] == 1:
                    next_state = (state[0] + direction[0], state[1] + direction[1])
                    group.append(next_state)
                    dfs(next_x, next_y, group, next_state)

        distinct_islands = set()
        rows, cols = len(grid), len(grid[0])
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 1:
                    group = []
                    dfs(x, y, group, (0, 0))
                    distinct_islands.add(tuple(group))

        return len(distinct_islands)
