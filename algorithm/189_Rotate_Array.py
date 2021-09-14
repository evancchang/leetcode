class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums) # if k > len(nums), we can find the same k steps
        nums[:] = nums[-k:] + nums[:-k]
        return nums
