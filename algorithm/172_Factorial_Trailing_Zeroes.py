class Solution:
    def trailingZeroes(self, n: int) -> int:
        zeros = 0
        
        while n > 0:
            n //= 5 # because 10 = 2*5, find the number of 5 because number of 2 is more than 5.
            zeros += n
            
        return zeros
