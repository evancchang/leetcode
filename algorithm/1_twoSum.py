class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash = {}

        for i in range(len(nums)):
            if target - nums[i] in hash.keys():
                return [hash[target - nums[i]], i]
                hash[nums[i]] = i

        return [-1, -1]


#nums = [2, 7, 11, 15]
#target = 9
#nums = [3,2,4]
#target = 6

nums = [2,1,9,4,4,56,90,3]
target = 8

t = Solution()
t.twoSum(nums, target)
