from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        minutes = 0
        fresh_count = 0
        rotten = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh_count += 1
                if grid[i][j] == 2:
                    rotten.append((i, j))

        while rotten and fresh_count > 0:
            minutes += 1
            
            for _ in range(len(rotten)):
                x, y = rotten.popleft()
                
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx = x + dx
                    ny = y + dy
                    
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        fresh_count -= 1
                        grid[nx][ny] = 2
                        rotten.append((nx, ny)) 

        if fresh_count == 0:
            return minutes
        else:
            return -1
