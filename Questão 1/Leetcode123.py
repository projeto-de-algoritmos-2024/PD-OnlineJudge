class Solution(object):
    def maxProfit(self, prices):
        cost = -999999
        cost2 = -999999 
        sell = 0
        sell2 = 0

        for price in prices:
            cost = max(cost, -price)
            sell = max(sell, cost + price)
            cost2 = max(cost2, sell - price)
            sell2 = max(sell2, cost2 + price)

        return sell2
