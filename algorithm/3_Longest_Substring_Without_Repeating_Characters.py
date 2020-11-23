class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        chars = set()
        
        l = 0
        while left < len(s) and right < len(s):
            if s[right] in chars:
                if s[left] in chars:
                    chars.remove(s[left])
                left += 1
            else:
                chars.add(s[right])
                right += 1                
                l = max(l, len(chars))
            
        return l

class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        ch_idx = {}
        i = 0
        for j, ch in enumerate(s):
            if ch in ch_idx:
                i = max(ch_idx[ch], i)
            ans = max(ans, j - i + 1)
            ch_idx[ch] = j + 1
            
        return ans
