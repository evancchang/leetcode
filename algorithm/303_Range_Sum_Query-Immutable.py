class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        len_n = len(nums)
        if len_n:
            self.total_nums = [0] * len_n
            self.total_nums[0] = nums[0]
        
            for i in range(1, len_n):
                self.total_nums[i] = self.total_nums[i-1] + nums[i]
        else:
            self.total_nums = [0]
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i > 0:
            return self.total_nums[j] - self.total_nums[i-1]
        else:
            return self.total_nums[j]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)



# Your NumArray object will be instantiated and called as such:
numArray = NumArray([-2, 0, 3, -5, 2, -1])
print numArray.sumRange(0, 1)
print numArray.sumRange(1, 2)
print numArray.sumRange(0, 2)
print numArray.sumRange(2, 5)
print numArray.sumRange(0, 5)
