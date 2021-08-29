class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        odd = []
        even = []
        for n in A:
            if n % 2 == 0:
                even.append(n)
            else:
                odd.append(n)
                
        return even + odd

class Solution2:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        slow = 0
        for fast in range(len(nums)): # use slow pointer to record the odd value idx
            if nums[fast] % 2 == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
                
        return nums        
