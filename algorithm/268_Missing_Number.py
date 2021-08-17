class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        for i in range(n):
            if i != nums[i]:
                return i
            
        return n
        
class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        total = (1 + n) * n / 2
        ans = int(total - sum(nums))
        
        return ans
