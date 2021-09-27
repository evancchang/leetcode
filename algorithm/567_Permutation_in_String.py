class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        sub_s_map = {}
        s_map = {}
        if n1 > n2:
            return False
        
        if n1 == n2:
            for ch in s1:
                if ch not in sub_s_map:
                    sub_s_map[ch] = 1
                else:
                    sub_s_map[ch] += 1
            for ch in s2:
                if ch not in s_map:
                    s_map[ch] = 1
                else:
                    s_map[ch] += 1
            return sub_s_map == s_map
        
        else: # n1 < n2
            for ch in s1:
                if ch not in sub_s_map:
                    sub_s_map[ch] = 1
                else:
                    sub_s_map[ch] += 1
            
            for i in range(n2 - n1 + 1):
                s = s2[i:i+n1]
                s_map = {}
                for ch in s:
                    if ch not in s_map:
                        s_map[ch] = 1
                    else:
                        s_map[ch] += 1
                
                if sub_s_map == s_map:
                    return True        

        return False
