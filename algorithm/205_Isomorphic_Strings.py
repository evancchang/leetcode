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
                
