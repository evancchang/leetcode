# Time Limit Exceed
#class Solution:
#    def climbStairs(self, n: int) -> int:
#        if n < 3:
#            return n
#        else:
#            return self.climbStairs(n - 1) + self.climbStairs(n - 2)

class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        else:
            a = 1
            b = 2
            for _ in range(2, n):
                c = a + b
                a = b
                b = c
                
            return c
