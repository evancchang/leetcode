class Solution:
    def sumZero(self, n: int) -> List[int]:
        l = n // 2
        
        if n % 2 == 0:
            ans = []
        else:
            ans = [0]
            
        for i in range(1, l+1):
            ans.append(i)
            ans.append(-i)
            
        return ans
