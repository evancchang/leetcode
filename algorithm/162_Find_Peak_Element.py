class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                return i
            
        return n-1
        
