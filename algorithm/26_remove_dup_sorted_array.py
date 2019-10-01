class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[count]:
                count += 1
                nums[count] = nums[i]
        
        return count + 1

t = Solution()
print t.removeDuplicates([1,1,2,2,3])
print t.removeDuplicates([])
