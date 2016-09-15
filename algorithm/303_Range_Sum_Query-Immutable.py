class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        if len(nums):
            # caculate the sum first.
            self.nums = [0] * len(nums)
            self.nums[0] = nums[0]

            for idx in xrange(1, len(nums)):
                # self.num[idx] = sumRange(0, idx)
                self.nums[idx] = self.nums[idx-1] + nums[idx]
        else:
            self.nums = [0]

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if i > 0:
            # sumRange(2, 5) = sumRange(0, 5) - sumRange(0, 1)
            return self.nums[j] - self.nums[i-1]
        else:
            return self.nums[j]



# Your NumArray object will be instantiated and called as such:
numArray = NumArray([-2, 0, 3, -5, 2, -1])
print numArray.sumRange(0, 1)
print numArray.sumRange(1, 2)
print numArray.sumRange(0, 2)
print numArray.sumRange(2, 5)
print numArray.sumRange(0, 5)
