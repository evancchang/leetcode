class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0
        for ch in stones:
            if ch in jewels:
                ans += 1
        return ans
