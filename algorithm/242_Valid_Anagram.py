class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_ch_d = {}
        for ch in s:
            if ch not in s_ch_d:
                s_ch_d[ch] = 1
            else:
                s_ch_d[ch] += 1
                
        for ch in t:
            curr_count = s_ch_d.get(ch, 0)
            if curr_count == 0:
                return False
            else:
                s_ch_d[ch] -= 1
                
        for k, v in s_ch_d.items():
            if v != 0:
                return False
            
        return True
