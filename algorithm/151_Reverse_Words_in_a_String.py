class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split()
        s_list.reverse()
        new_s = ''
        for ch in s_list:
            if ch.strip() != '':
                new_s += ' ' + ch

        return new_s.strip()        
