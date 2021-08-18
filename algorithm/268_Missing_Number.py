class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()  
        for i, val in enumerate(nums):
            if i != val:
                return i
            
        return len(nums)
        
class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = (0 + n) * (n + 1) / 2        
        ans = int(total) - sum(nums)
        
        return ans
