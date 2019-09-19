class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # because 10 = 2x5, find the numbers of '5'.
        res = 0
        while n > 0:
            n /= 5
            res += n

        return res
