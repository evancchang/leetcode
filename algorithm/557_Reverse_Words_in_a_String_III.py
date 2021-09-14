class Solution:
    def reverseWords(self, s: str) -> str:
        s = s[::-1]
        s = s.split()
        s = s[::-1]
        return ' '.join(s)

class Solution2:
    def reverseWords(self, s: str) -> str:
        s_list = s.split()
        ans = ''
        for s in s_list:
            ans += s[::-1] + ' '
            
        return ans.strip()
