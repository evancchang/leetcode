class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        
        for ch in s:
            if ch not in s_dict:
                s_dict[ch] = 1
            else:
                s_dict[ch] += 1
                
        for ch in t:
            if ch not in t_dict:
                t_dict[ch] = 1
            else:
                t_dict[ch] += 1
                
        if s_dict == t_dict:
            return True
        else:
            return False

 class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
