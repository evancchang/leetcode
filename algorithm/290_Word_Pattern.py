class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        s_list = str.split()
        if len(pattern) != len(s_list):
            return False
        p_dict = {}
        
        for i in range(len(pattern)):
            if pattern[i] not in p_dict.keys() and s_list[i] not in p_dict.values():
                p_dict[pattern[i]] = s_list[i]
            else:
                if pattern[i] not in p_dict.keys() and s_list[i] in p_dict.values():
                    return False
                if p_dict[pattern[i]] != s_list[i]:
                    return False         
              
        return True

t = Solution()
print t.wordPattern('abba', 'dog dog dog dog')
