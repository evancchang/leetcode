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

class Solution2:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2) + int(b,2))[2:]
