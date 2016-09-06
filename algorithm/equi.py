def solution(A):    
    if len(A) == 0:
        return -1
        
    lsum = 0
    rsum = sum(A)
    target = []
    for index, value in enumerate(A):
    	rsum -= value
    	if lsum == rsum:
    		return index   		
		lsum += value

solution([-1,3,-4,5,1,-6,2,1])
