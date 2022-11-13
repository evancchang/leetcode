class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        left = 0
        right = n - 1
        start_pos = self.find_start_pos(nums, left, right, target)
        end_pos = self.find_end_pos(nums, left, right, target)

        return [start_pos, end_pos]

    def find_start_pos(self, nums, left, right, target):
        res = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                res = mid
                right = mid -1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return res

    def find_end_pos(self, nums, left, right, target):
        res = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                res = mid
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return res

class Solution2:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search_left(nums, target):
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = (left+right) // 2
                guess = nums[mid]
                if guess < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        def binary_search_right(nums, target):
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = (left+right) // 2
                guess = nums[mid]
                if guess <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        start_pos = binary_search_left(nums, target)
        end_pos = binary_search_right(nums, target)
        if start_pos <= end_pos:
            return [start_pos, end_pos]
        else:
            return [-1, -1]    
