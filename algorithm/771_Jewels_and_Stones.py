class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        ans = 0
        for ch in J:
            for c in S:
                if ch == c:
                    S.replace(ch, '', 1)
                    ans += 1
                
        return ans
        
