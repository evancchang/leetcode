class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        highest_num = -1
        second_high_num = -1
        highest_idx = -1
        
        for i, num in enumerate(nums):
            if num > highest_num:
                second_high_num = highest_num
                highest_num = num
                highest_idx = i
            elif num > second_high_num:
                second_high_num = num
                
        if highest_num >= (2 * second_high_num):
            return highest_idx
        else:
            return -1
        
