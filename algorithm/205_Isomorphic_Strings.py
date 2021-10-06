class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
            
        # use 2 dict to check the mapping relationship.
        s_dict = {}
        t_dict = {}
        
        for i in xrange(len(s)):
            if s[i] in s_dict.keys() and s_dict[s[i]] != t[i]:
                return False
            if t[i] in t_dict.keys() and t_dict[t[i]] != s[i]:
                return False
                
            s_dict[s[i]] = t[i]
            t_dict[t[i]] = s[i]
            
        return True
                
class Solution2:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_map = {}
        t_map = {}
        
        n = len(s)
        for i in range(n):
            s_map[s[i]] = t[i]
            t_map[t[i]] = s[i]
            
        cmp_str1 = ''
        for ch in s:
            cmp_str1 += s_map[ch]
            
        cmp_str2 = ''
        for ch in t:
            cmp_str2 += t_map[ch]
            
        return (cmp_str1 == t) and (cmp_str2 == s)

class Solution3:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}
        
        for ch_s, ch_t in zip(s, t):
            if (ch_s not in s_map) and (ch_t not in t_map):
                s_map[ch_s] = ch_t
                t_map[ch_t] = ch_s
            else:
                if s_map.get(ch_s) != ch_t or t_map.get(ch_t) != ch_s:
                    return False
                
        return True    
