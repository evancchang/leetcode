class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        
        len_nee = len(needle)
        len_hay = len(haystack)
        
        for i in range(len_hay - len_nee + 1):
            if haystack[i:i+len_nee] == needle:
                return i
            
        return -1
