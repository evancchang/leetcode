from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        resp = 0
        c = Counter(s)
        for k, v in c.items():
            resp += v // 2 * 2
            if resp % 2 == 0 and v % 2 == 1:
                resp += 1
                
        return resp
        
