class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(int(num**0.5) + 1):
            if i * i == num:
                return True
        return False

class Solution2:
    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = int(num**0.5) + 1
        
        while left <= right:
            mid = (left + right) // 2
            val = mid * mid
            
            if val == num:
                return True
            elif val > num:
                right = mid - 1
            else:
                left = mid + 1
                
        return False    
