class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
                    
        return count
    
    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = 'v' # visited
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
                    
from collections import deque
class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.bfs(grid, i, j)
                    count += 1
                    
        return count
    
    def bfs(self, grid, i, j):
        q = deque()
        q.append((i,j))
        grid[i][j] = 'v'

        direction = [(0,1), (0,-1), (1,0), (-1,0)]
        while q:
            x, y = q.popleft()
            for d in direction:
                nx = x + d[0]
                ny = y + d[1]
                if (0<=nx<len(grid)) and (0<=ny<len(grid[0])) and grid[nx][ny] == '1':
                    q.append((nx,ny))
                    grid[nx][ny] = 'v'
