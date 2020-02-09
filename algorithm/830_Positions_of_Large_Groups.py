class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        resp = []
        count = 1
        ch = S[0]
        start = end = 0
        for i in range(1, len(S)):
            if ch == S[i]:
                count += 1
                end += 1
            else:
                if count >= 3:
                    resp.append([start, end])
                    
                ch = S[i]
                count = 1
                start = end = i
        if count >= 3:
            resp.append([start, end])
                
        return resp
