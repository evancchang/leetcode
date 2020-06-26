class Solution:
    def isHappy(self, n: int) -> bool:
        got = set()
        while n != 1 and n not in got:
            got.add(n)
            s = 0
            while n:
                s += (n % 10) ** 2
                n //= 10
                
            n = s
            
        return n == 1
