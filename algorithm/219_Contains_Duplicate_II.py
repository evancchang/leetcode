class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) < 2:
            return False
            
        hash_table = {}
        for i, num in enumerate(nums):
            if num in hash_table and (i-hash_table[num]<=k):
                return True
            else:
                hash_table[num] = i
                
        return False
