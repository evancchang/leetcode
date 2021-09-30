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

class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float('-inf')
        accumulate = 0
        
        for num in nums:
            accumulate += num
            ans = max(ans, accumulate)
            if accumulate < 0:
                accumulate = 0
                
        return ans
