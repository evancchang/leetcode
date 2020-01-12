class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        sx = bin(x)[2:].zfill(32)
        sy = bin(y)[2:].zfill(32)
        
        return sum(elx != ely for elx, ely in zip(sx, sy))
        
