class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            sign = 1
        else:
            sign = -1
            x = abs(x)

        ans = 0
        while x:
            ans = ans * 10 + x % 10
            x /= 10

        reverse_out = sign *ans

        if  ((reverse_out > 2147483647)or(reverse_out < -2147483648)): # handle 32-bit overflow            
            return 0
        else:
            return reverse_out

t = Solution()
#print t.reverse(1534236469)
print t.reverse(1)
