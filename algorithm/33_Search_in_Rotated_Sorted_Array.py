class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            guess = nums[mid]
            if target == guess:
                return mid
            elif nums[left] <= guess:
                if nums[left] <= target <= guess:
                    right = mid - 1
                else:
                    left = mid + 1 
            else:
                if guess <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid -1
        return -1
