class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        
        ans = 0
        for i in range(0, n, 2):
            ans += nums[i]
            
        return ans
        
