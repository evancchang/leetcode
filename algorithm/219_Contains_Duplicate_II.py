class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        
        h = {}
        for i in range(len(nums)):
            if nums[i] in h.keys() and (i - h[nums[i]] <= k):
                return True
            else:
                h[nums[i]] = i
                
        return False
