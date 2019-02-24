# https://leetcode.com/problems/minimum-path-sum/


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        n, m = len(grid), len(grid[0])
        min_path = [0] * m
        min_path[0] = grid[0][0]

        for i in range(1, m):
            min_path[i] = min_path[i - 1] + grid[0][i]

        for i in range(1, n):
            min_path[0] += grid[i][0]
            for j in range(1, m):
                min_path[j] = min(min_path[j - 1], min_path[j]) + grid[i][j]

        return min_path[-1]


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        n, m = len(grid), len(grid[0])
        for i in range(1, m):
            grid[0][i] += grid[0][i - 1]

        for i in range(1, n):
            grid[i][0] += grid[i - 1][0]

        for i in range(1, n):
            for j in range(1, m):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[-1][-1]
