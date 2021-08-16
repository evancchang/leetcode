class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float("-inf")
        prev, curr = 0, 0
        
        for i, val in enumerate(nums):
            curr = val + prev
            if curr > 0:
                prev = curr
            else:
                prev = 0

            ans = max(ans, curr)

        return ans
        
