class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        n = numRows + 1
        ret = []
        for i in range(1, n):
            if i == 1:
                ret.append([1])
            elif i == 2:
                ret.append([1, 1])
            else:
                prev = ret[i - 2] # ret[i - 1 - 1]
                curr = [0] * i
                curr[0] = prev[0]
                for j in range(1, i - 1):
                    curr[j] = prev[j] + prev[j - 1]
                    
                curr[-1] = prev[-1]
                ret.append(curr)
                
        return ret
                
        
