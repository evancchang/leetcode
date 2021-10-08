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
    
class Solution2:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        tmp_sum = {}
        ans = 0
        
        for i in nums1:
            for j in nums2:
                tmp = i + j
                if tmp not in tmp_sum:
                    tmp_sum[tmp] = 1
                else:
                    tmp_sum[tmp] += 1
                    
        for k in nums3:
            for l in nums4:
                tmp = k + l
                ans += tmp_sum.get(-tmp, 0)
                
        return ans
