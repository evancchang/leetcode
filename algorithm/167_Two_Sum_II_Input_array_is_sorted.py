class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_idx = {}
        for i, num in enumerate(numbers):
            val = target - num
            if val in num_idx:
                return [num_idx[val], i+1]
            else:
                num_idx[num] = i+1
