class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0
        
        for i in range(2, n):
            count += self.isPrime(i)
        
        return count
    
    def isPrime(self, n):
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return 0
        return 1
                
class Solution2:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        
        primes = [True] * (n)
        primes[0] = primes[1] = False
        for i in range(2, int(n**0.5)+1):
            if primes[i]:
                for j in range(i+i, n, i):
                    primes[j] = False
                    
        count = 0
        for i in range(2, n):
            if primes[i]:
                count += 1
        return count
        
                
