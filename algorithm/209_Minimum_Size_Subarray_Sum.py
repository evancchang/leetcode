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
        
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        slow = 0
        total = 0
        min_len = float('inf')

        for fast, num in enumerate(nums):
            total += num
            while total >= target:
                min_len = min(min_len, fast - slow + 1)
                total -= nums[slow]
                slow += 1

        if min_len != float('inf'):
            return min_len
        else:
            return 0
