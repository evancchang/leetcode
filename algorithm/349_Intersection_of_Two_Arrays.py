class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for num1 in nums1:
            if num1 in nums2:
                if num1 not in ans:
                    ans.append(num1)
                
        return ans        

class Solution2:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        
        return list(set1&set2)
