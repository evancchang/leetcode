from collections import defaultdict
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        ans = 0
        result = defaultdict(int)
        
        for i in nums1:
            for j in nums2:
                result[i+j] += 1
                
        for k in nums3:
            for l in nums4:
                ans += result[-(k+l)]
                    
        return ans
