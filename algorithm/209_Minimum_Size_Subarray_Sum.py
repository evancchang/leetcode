class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        slow = 0
        total = 0
        ans = float('inf')
        for fast in range(len(nums)):
            total += nums[fast]
            while total >= target:
                ans = min(ans, fast - slow + 1)        
                total -= nums[slow]
                slow += 1
            
        if ans != float('inf'):
            return ans
        else:
            return 0
