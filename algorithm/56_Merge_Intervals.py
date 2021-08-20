class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        ans = []
        
        for interval in intervals:
            if not ans or ans[-1][1] < interval[0]: # not overlap case
                ans.append(interval)
            else: # overlap case
                ans[-1][1] = max(ans[-1][1], interval[1])
                
        return ans
