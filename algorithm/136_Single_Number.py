class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        h = {}
        
        for i in nums:
            if i not in h.keys():
                h[i] = 1
            else:
                h[i] += 1
                
        for k in h.keys():
            if h[k] == 1:
                return k
            
        return -1
