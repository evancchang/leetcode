class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        out = int(a, 2) + int(b, 2)
        out = bin(out)[2:] # remove 0b

        return out

t = Solution()
print t.addBinary('11', '1')
