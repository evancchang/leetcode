class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(1, numRows + 1):
            if i == 1:
                tmp = [1]
            elif i == 2:
                tmp = [1,1]
            else:
                tmp = [1] * i
                for i in range(i - 2):
                    tmp[i+1] = ans[-1][i] + ans[-1][i+1]
            ans.append(tmp)
        return ans
        
