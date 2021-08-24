from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        return c.most_common(1)[0][0]

class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        num_count = {}
        
        for num in nums:
            if num in num_count:
                num_count[num] += 1
            else:
                num_count[num] = 1
                
        n = len(nums) // 2
        for k, v in num_count.items():
            if v > n:
                return k
