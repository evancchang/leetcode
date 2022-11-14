class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ch_set = set() # use set to add/remove item, the bigO is O(1) average
        left = right = 0
        length = 0
        n = len(s)

        while left < n and right < n:
            if s[right] not in ch_set:
                ch_set.add(s[right])
                right += 1
            else:
                if s[left] in ch_set:
                    ch_set.remove(s[left])
                    left += 1
            length = max(length, len(ch_set))
        return length    
    
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
