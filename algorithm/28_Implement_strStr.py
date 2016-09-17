class Solution(object):
    def strStr(self, haystack, needle):
		"""
		:type haystack: str
		:type needle: str
		:rtype: int
		"""
		if (not haystack) and (not needle):
			return 0

		if len(haystack) >= len(needle):
			for i in xrange(len(haystack)-len(needle)+1):
				if haystack[i:i+len(needle)] == needle:
					return i
			return -1
		else:
			return -1


t = Solution()
print t.strStr("a", "a")
