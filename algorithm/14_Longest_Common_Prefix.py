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

class Solution2:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=lambda x:len(x))
        n = len(strs[0])
        
        ans = ''
        need_break = False
        for i in range(n):
            curr_ch = strs[0][i]
            for j in range(1, len(strs)):
                if curr_ch != strs[j][i]:
                    need_break = True
                    break
            if need_break:
                break
            
            ans += curr_ch
            
        return ans
