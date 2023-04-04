class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        total = 0
        buy = 0
        sell = 0
        for _ in range(len(prices)):
            if prices[buy] < prices[sell]:
                total += prices[sell] - prices[buy]
            buy = sell
            sell += 1
        
        return total