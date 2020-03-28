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

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        min_price = float("inf")
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)
                
        return max_profit
    
t = Solution()
#print t.maxProfit([7,1,5,3,6,4])
print t.maxProfit([2,4,1])
