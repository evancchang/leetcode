class Solution:
    def firstUniqChar(self, s: str) -> int:
        h = {}
        s = s.lower()
        
        for i in range(len(s)):
            if s[i] not in h:
                h[s[i]] = i
            else:
                h[s[i]] = -1
                
        ans = float('inf')
        for key, value in h.items():
            if value != -1:
                if ans > value:
                    ans = value
                    
        if ans < float('inf'):
            return ans
        else:
            return -1
        
            
