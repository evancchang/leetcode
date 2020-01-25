from collections import Counter
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        n = len(A)
        c = Counter(A[0])
        
        for i in range(1, n):
            c &= Counter(A[i])
            
        return list(c.elements())
            
