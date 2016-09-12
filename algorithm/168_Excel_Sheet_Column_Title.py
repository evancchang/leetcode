class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        out_str = ""
        while n:
            out_str = chr((n-1)%26+65) + out_str # chr(65) = 'A'
            n = (n-1)/26

        return out_str

t = Solution()
#print t.convertToTitle(1)
print t.convertToTitle(26)
#print t.convertToTitle(53)
