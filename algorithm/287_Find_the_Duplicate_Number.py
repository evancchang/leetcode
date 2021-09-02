class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        num_set = set()
        
        for num in nums:
            if num not in num_set:
                num_set.add(num)
            else:
                return num
