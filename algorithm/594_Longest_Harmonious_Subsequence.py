from collections import Counter
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        longest = 0
        c = Counter(nums)
        for n in c:
            if (n + 1) in c:
                longest = max(longest, c[n] + c[n+1])
                
        return longest
        
