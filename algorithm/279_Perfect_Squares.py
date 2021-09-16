from collections import deque
class Solution:
    def numSquares(self, n: int) -> int:
        sq_list = []
        q = deque()
        count = 1
        for i in range(1, int(n**0.5)+1):
            sq_list.append(i**2)
        q.append(n)    
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                for sq in sq_list:
                    if node == sq:
                        return count
                    if node < sq:
                        break
                    else:
                        q.append(node-sq)
            count += 1 # Add 1 to steps to go to the next level as we were not able to find target in this level 
            
        
                
        
