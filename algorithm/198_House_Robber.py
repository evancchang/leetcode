class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        elif n <= 2:
            return max(nums[0], nums[-1])
        
        money = [0] * n
        money[0], money[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            money[i] = max(nums[i] + money[i-2], money[i-1])
            
        return money[-1]
