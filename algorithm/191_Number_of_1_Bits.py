class Solution:
    def hammingWeight(self, n: int) -> int:
        sn = bin(n).strip('0b')
        out = 0
        for i in range(len(sn)):
            if sn[i] == '1':
                out += 1
                
        return out
        
