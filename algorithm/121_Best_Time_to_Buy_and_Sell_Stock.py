#class Solution:
#    def maxProfit(self, prices: List[int]) -> int:
#        if not prices:
#            return 0
#        
#        lowest_price = prices[0]
#        profit = 0
#        for day in range(1, len(prices)):
#            profit = max(profit, prices[day] - lowest_price)
#            lowest_price = min(lowest_price, prices[day])
#            
#        return profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        lowest_price = prices[0]
        max_profit = 0
        for day in range(1, len(prices)):
            if lowest_price > prices[day]:
                lowest_price = prices[day]
                
            if prices[day] - lowest_price > max_profit:
                max_profit = prices[day] - lowest_price
            
        return max_profit

t = Solution()
#print t.maxProfit([7,1,5,3,6,4])
print t.maxProfit([2,4,1])
