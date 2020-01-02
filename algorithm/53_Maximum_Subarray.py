class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        prev, curr = 0, 0
        ans = float("-inf")
        for i in range(n):
            curr = nums[i] + prev    
            if curr > 0:
                prev = curr
            else:
                prev = 0
                
            ans = max(ans, curr)
                
        return ans
        
