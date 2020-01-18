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
