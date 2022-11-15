class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for m in matrix:
            for n in m:
                if n == target:
                    return True
        return False        

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for mat in matrix:
            result = self.binary_search(mat, target)
            if result:
                return result
        return result

    def binary_search(self, lis, target):
        left = 0
        right = len(lis) - 1

        while left <= right:
            mid = (left + right) // 2
            guess = lis[mid]
            if guess == target:
                return True
            elif guess > target:
                right = mid - 1
            else:
                left = mid + 1
        return False 
