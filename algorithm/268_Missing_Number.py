class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if len(nums) == 1 and nums[0] != 1:
            return 1
        
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)
        
