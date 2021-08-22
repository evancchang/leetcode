class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tri_list = []
        
        for i in range(1, numRows + 1):
            if i == 1:
                tri_list.append([1])
            elif i == 2:
                tri_list.append([1,1])
            else:
                prev = tri_list[i - 1 - 1]
                curr = [0] * i
                curr[0] = prev[0]
                for j in range(len(prev) - 1):
                    curr[j+1] = prev[j] + prev[j+1]
                curr[-1] = prev[-1]
                tri_list.append(curr)

        return tri_list
                
        
