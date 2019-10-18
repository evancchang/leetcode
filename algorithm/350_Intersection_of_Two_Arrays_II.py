class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        n1_map = {}
        
        for n in nums1:
            if n not in n1_map.keys():
                n1_map[n] = 1
            else:
                n1_map[n] += 1
                
        for n in nums2:
            if n in n1_map.keys() and n1_map[n] > 0:
                ans.append(n)
                n1_map[n] -= 1
                
        return ans
        
        
