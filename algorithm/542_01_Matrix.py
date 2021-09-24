from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        visited = set()
        q = deque()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    visited.add((i,j))
                    q.append((i,j))
        while q:
            x, y = q.popleft()
            for dir in [(1,0), (-1, 0), (0, 1), (0, -1)]:
                nx = x + dir[0]
                ny = y + dir[1]

                if (0<=nx<len(mat)) and (0<=ny<len(mat[0])) and (nx, ny) not in visited:
                    mat[nx][ny] = mat[x][y] + 1
                    visited.add((nx, ny))
                    q.append((nx,ny))
        return mat
