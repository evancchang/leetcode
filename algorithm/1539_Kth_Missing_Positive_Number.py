class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        miss_count = 0
        max_val = arr[-1]
        
        for i in range(1, max_val+1):
            if i not in arr:
                miss_count += 1
                if miss_count == k:
                    return i
                
        remain = k - miss_count
        return max_val + remain
