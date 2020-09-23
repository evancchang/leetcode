class Solution:
    def titleToNumber(self, s: str) -> int:
        ans = 0
        for i, ch in enumerate(s):
            ans *= 26
            ans += ord(ch) - 64
            
        return ans
