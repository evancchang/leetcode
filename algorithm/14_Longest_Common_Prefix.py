class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        if not strs:
            return res
        
        strs.sort()
        for i in range(len(strs[0])):
            if strs[0][i] != strs[-1][i]:
                break
            else:
                res += strs[0][i]
                
        return res

t = Solution()
#print t.longestCommonPrefix(['awbc', 'ab', 'aebcde'])
print t.longestCommonPrefix(['a', 'a', 'b'])
