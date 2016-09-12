class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1: return -1
        if n == 1: return 0

        if n > 1:
            step = 0
            while n != 1:
                if (n % 2 == 0):
                    n >>= 1
                    step += 1
                elif n == 3:
                    n = 2
                    step += 1
                else:
                    # The more tail zero numbers, the less steps.
                    if (self.countTailZero(n-1) > self.countTailZero(n+1)):
                        n -= 1
                    else:
                        n += 1

                    step += 1

            return step

    def countTailZero(self, n):
        """count all tail zero numbers in binary."""
        i = 0
        while (n & 1 == 0):
            n >>= 1
            i +=1

        return i

t = Solution()
#print t.integerReplacement(65535)
print t.integerReplacement(3)
#print t.integerReplacement(8)
#print t.integerReplacement(7)
#print t.integerReplacement(3)
#print t.integerReplacement(0)
#print t.integerReplacement(1)
