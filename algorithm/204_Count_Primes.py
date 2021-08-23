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
        if n == 0:
            prime = [False]
        elif n == 1:
            prime = [False, False]
        else:
            prime = [True for i in range(n)]
            p = 2
            while (p * p < n):
                if prime[p]:
                    for i in range(p + p, n, p):
                        prime[i] = False
                    
                p += 1
            prime[0] = False
            prime[1] = False
        
        ans = 0
        for i in range(n):
            if prime[i]:
                ans += 1
                
        return ans
        
                
