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
