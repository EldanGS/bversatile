# https://leetcode.com/problems/number-of-islands/


class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        def modify_island(x, y):
            grid[x][y] = '0'
            for next_x, next_y in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= next_x < len(grid) and 0 <= next_y < len(grid[next_x]) and grid[next_x][next_y] == '1':
                    modify_island(next_x, next_y)

        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    num_islands += 1
                    modify_island(i, j)

        return num_islands

