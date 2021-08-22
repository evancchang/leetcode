from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        return c.most_common(1)[0][0]

class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        num_counts = {}
        major_count = 0
        major_element = 0
        
        for num in nums:
            if num not in num_counts:
                num_counts[num] = 1
            else:
                num_counts[num] += 1
                
        times = len(nums) // 2
        
        for k, v in num_counts.items():
            if v > times:
                if v > major_count:
                    major_count = v
                    major_element = k
                
        return major_element
