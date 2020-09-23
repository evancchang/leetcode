class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_place_dict = {}
        for i, num in enumerate(nums):
            result = target - num
            if result in nums_place_dict.keys():
                return [nums_place_dict[result], i]
            nums_place_dict[num] = i


#nums = [2, 7, 11, 15]
#target = 9
#nums = [3,2,4]
#target = 6

nums = [2,1,9,4,4,56,90,3]
target = 8

t = Solution()
t.twoSum(nums, target)
