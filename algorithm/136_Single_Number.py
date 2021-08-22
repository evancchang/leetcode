class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for n in nums:
            result ^= n # use XOR
            
        return result

class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        num_counts = {}
        
        for num in nums:
            if num not in num_counts:
                num_counts[num] = 1
            else:
                num_counts[num] += 1
                
        for k, v in num_counts.items():
            if v == 1:
                return k
