class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        curr_color = image[sr][sc]
        if curr_color == newColor:
            return image
        
        def dfs(x, y):
            if x < 0 or y < 0 or x >= m or y >= n or image[x][y] != curr_color:
                return
            image[x][y] = newColor
            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)
        
        dfs(sr, sc)
        return image
