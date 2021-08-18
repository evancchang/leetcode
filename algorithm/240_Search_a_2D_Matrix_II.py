class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for m in matrix:
            for n in m:
                if n == target:
                    return True
        return False        
