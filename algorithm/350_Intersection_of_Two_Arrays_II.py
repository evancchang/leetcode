class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        nums1_count = {}
        
        for num in nums1:
            if num not in nums1_count:
                nums1_count[num] = 1
            else:
                nums1_count[num] += 1
                
        for num in nums2:
            if num in nums1_count:
                if nums1_count[num] > 0:
                    ans.append(num)
                    nums1_count[num] -= 1
                    
        return ans
        
        
