class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length:
            idx = 1
            for i in range(1, length):
                if nums[i] != nums[i-1]:
                    nums[idx] = nums[i]
                    idx += 1

            #nums = nums[:idx]
            return idx
        else:
            return length

t = Solution()
print t.removeDuplicates([1,1,2,2,3])
print t.removeDuplicates([])
