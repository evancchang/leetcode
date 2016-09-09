class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        lowest_price = prices[0]
        profit = 0
        total_days = len(prices)

        for i in range(total_days):
            profit = max(profit, prices[i] - lowest_price)
            lowest_price = min(prices[i], lowest_price)

        return profit

t = Solution()
#print t.maxProfit([7,1,5,3,6,4])
print t.maxProfit([2,4,1])
