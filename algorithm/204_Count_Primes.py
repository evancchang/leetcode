import math
class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0
        for i in range(2, n):
            count += self.is_Primes(i)
            
        return count    
        
        
    def is_Primes(self, n: int) -> int:
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return 0
        return 1
        
                
