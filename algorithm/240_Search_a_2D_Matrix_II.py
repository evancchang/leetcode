class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for m in matrix:
            for n in m:
                if n == target:
                    return True
        return False        

class Solution2:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for m in matrix:
            print(f'm = {m}')
            if self.binarySearch(m, target):
                return True
        return False
    
    def binarySearch(self, l, item):
        low = 0
        high = len(l) - 1
        
        while low <= high:
            mid = (low + high) // 2
            guess = l[mid]
            if guess == item:
                return True
            elif guess > item:
                high = mid - 1
            else:
                low = mid + 1
                
        return False   
