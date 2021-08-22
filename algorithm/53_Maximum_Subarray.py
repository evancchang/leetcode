class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = float('-inf')
        prev = 0
        
        for num in nums:
            curr = num + prev
            
            if curr > 0:
                prev = curr
            else:
                prev = 0
                
            total = max(total, curr)
                
        return total
