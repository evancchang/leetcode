class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows == 1:
            return s

        zigzag = ""
        step = 2 * numRows - 2
        for i in xrange(numRows):
            for j in xrange(i, len(s), step):
                zigzag += s[j]
                print("i = %d" %i)
                print("j = %d" %j)
                print("s = %s" %s)
                print("zigzag = %s" %zigzag)
                if 0 < i < numRows - 1 and j + step - 2 * i < len(s):
                    zigzag += s[j + step - 2 * i]
                    print(">>> zigzag = %s" %zigzag)
        return zigzag

t = Solution()

#print t.convert("ABC", 2)
print t.convert("PAYPALISHIRING", 3)
