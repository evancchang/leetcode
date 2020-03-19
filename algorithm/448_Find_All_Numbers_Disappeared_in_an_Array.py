class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = set(nums)
        exp = set(range(1, len(nums) + 1))
        return list(exp - n)
            
