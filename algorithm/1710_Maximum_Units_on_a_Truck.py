class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:x[1], reverse=True)
        ans = 0
        
        for num, unit in boxTypes:
            num = min(num, truckSize)
            ans += num * unit
            truckSize -= num
            
            if truckSize == 0:
                break
        return ans
