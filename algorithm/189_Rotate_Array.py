class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums[:] = nums[-k:] + nums[:-k]
        

t = Solution()
#print t.rotate([1,2,3,4,5,6,7], 3)
#print t.rotate([1,2,3,4,5,6,7], 0)
print t.rotate([1,2], 1)
