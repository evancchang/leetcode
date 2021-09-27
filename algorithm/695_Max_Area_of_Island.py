class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count = max(self.dfs(grid, i, j), count)
                    
        return count
                    
    def dfs(self, grid, x, y):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] != 1:
            return 0
        grid[x][y] = 'v'
        right = self.dfs(grid, x+1, y)
        left = self.dfs(grid, x-1, y)
        up = self.dfs(grid, x, y+1)
        down = self.dfs(grid, x, y-1)
        return 1 + right + left + up + down
