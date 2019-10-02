class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if (not haystack) and (not needle):
            return 0
        
        len_hay = len(haystack)
        len_nee = len(needle)
        
        if len_hay >= len_nee:
            for i in range(len_hay-len_nee+1):
                if haystack[i:i+len_nee] == needle:
                    return i
                 
        return -1


t = Solution()
print t.strStr("a", "a")
