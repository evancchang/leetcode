class Solution:
    def firstUniqChar(self, s: str) -> int:
        ch_count = {}

        for ch in s:
            if ch not in ch_count:
                ch_count[ch] = 1
            else:
                ch_count[ch] += 1

        for i in range(len(s)):
            if ch_count[s[i]] == 1:
                return i
        return -1
        
            
