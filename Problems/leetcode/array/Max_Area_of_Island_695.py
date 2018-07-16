# https://leetcode.com/problems/max-area-of-island/description/

"""
Solution.
Complexity analysis:
Time: O(N) - always
Memory: O(1) - always
"""
class Solution:    
    def maxAreaOfIsland(self, grid):
        n = len(grid)
        m = len(grid[0])

        def dfs(x, y):
            if (0 <= x and x < n) and (0 <= y and y < m) and grid[x][y]:
                grid[x][y] = 0
                return 1 + dfs(x - 1, y) + dfs(x + 1, y) + dfs(x, y - 1) + dfs(x, y + 1)
            return 0
        
        islands = [dfs(i, j) for i in range(n) for j in range(m) if grid[i][j]]
        
        return max(islands) 
        