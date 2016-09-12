class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s[::-1]
        return s

t = Solution()
print t.reverseString("Hello world")
print t.reverseString("Hi Hi ")
