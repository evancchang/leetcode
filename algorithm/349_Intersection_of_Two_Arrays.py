class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for num1 in nums1:
            if num1 in nums2:
                if num1 not in ans:
                    ans.append(num1)
                
        return ans        
