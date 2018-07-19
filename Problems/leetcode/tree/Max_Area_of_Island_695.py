# https://leetcode.com/problems/max-area-of-island/description/

"""
1st solution.
Used: DFS algortihm
Complexity analysis:
Time: O((N * M)^2)
Memory: O(N * M) in worst case, stack memory
"""

class Solution:
    def maxAreaOfIsland(self, grid):
        n = len(grid)
        m = len(grid[0])
        
        def dfs(x, y):
            if (0 <= x and x < n) and (0 <= y and y < m) and grid[x][y]:
                grid[x][y] = 0
                return dfs(x + 1, y) + dfs(x - 1, y) + dfs(x, y + 1) + dfs(x, y - 1) + 1
            return 0
        
        max_area = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    max_area = max(max_area, dfs(i, j))
    
        return max_area
                
"""
2nd solution.
Used: BFS algortihm
Complexity analysis:
Time: O((N * M) * (N + M))
Memory: O(N * M) in worst case
"""

class Solution:
    def maxAreaOfIsland(self, grid):
        n = len(grid)
        m = len(grid[0])
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        
        max_area = 0
        current_area = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    current_area = 0
                    queue = [(i, j)]
                    grid[i][j] = 0
                    
                    while queue:
                        x = queue[0][0]
                        y = queue[0][1]
                        queue.pop(0)
                        current_area += 1
                        
                        for k in range(4):
                            nextX = x + dx[k]
                            nextY = y + dy[k]
                            
                            if (0 <= nextX and nextX < n) and (0 <= nextY and nextY < m) and grid[nextX][nextY]:
                                queue.append((nextX, nextY))
                                grid[nextX][nextY] = 0
                                
                max_area = max(max_area, current_area)   
    
        return max_area
                
        