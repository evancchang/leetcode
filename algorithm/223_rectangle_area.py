class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
		"""
		:type A: int
		:type B: int
		:type C: int
		:type D: int
		:type E: int
		:type F: int
		:type G: int
		:type H: int
		:rtype: int
		"""				                	
		total = ((abs(C-A) * abs(D-B)) + (abs(G-E) * abs(H-F)))
		if E>=C or A>=G or B>=H or F>=D: # if not overlap
		#if ((E>=C or F>=D) or (A>=G or B>=H) or (A>=G or F>=D) or (E>=C or B>=H)):
			return total
		
		xl = max(A, E)                        
		yl = max(B, F)                    
		xr = min(C, G)            
		yr = min(D, H)            
    
		print xr
		print xl
		print yr
		print yl    
		overlap = (abs(xr - xl) * abs(yr - yl))

		total = ((abs(C-A) * abs(D-B)) + (abs(G-E) * abs(H-F))) - overlap
		return total
        
t = Solution()
#print t.computeArea(-3, 0,3,4,0,-1,9,2)                
#print t.computeArea(0,0,0,0,-1,-1,1,1)                

print t.computeArea(-2,-2,2,2,-1,4,1,6)
